import os
import os.path
import sqlite3


class StudentsModal:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "TMS.db")

    def get_all_students(self):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM students ORDER BY id")
            data = cur.fetchall()
            return data

    def insert_student(self, s):
        student_values = (
            s['name'], int(s['age']), s['address'], s['gender'], s['course'], s['time_slot'], s['facilities'],
            s['picture'])
        # print(student_values)
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO students(name, age, address, gender, course, time_slot, facilities, picture) VALUES(?,?,?,?,?,?,?,?)",
                student_values)
            con.commit()
            return cur.rowcount

    def find_stud_by_id(self, stud_id):
        with sqlite3.connect(self.db_path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM students WHERE id=?", (stud_id,))
                return cur
            except sqlite3.Error as e:
                return ("Database error: %s" % e)
            except Exception as e:
                return ("Exception in _query: %s" % e)
