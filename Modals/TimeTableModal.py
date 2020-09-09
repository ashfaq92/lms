import os
import sqlite3
import os.path


class TimeTableModal:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "TMS.db")

    def get_time_table_by_student_id(self, stud_id):
        with sqlite3.connect(self.db_path) as con:
            # con.row_factory = sqlite3.Row
            cur = con.cursor()
            try:
                str_stud_id = '%' + str(stud_id) + '%'
                cur.execute("SELECT * FROM time_table WHERE student_id LIKE ?", (str_stud_id,))
                return cur
            except sqlite3.Error as e:
                return ("Database error: %s" % e)
            except Exception as e:
                return ("Exception in _query: %s" % e)

    def get_time_table_by_faculty_id(self, fac_id):
        with sqlite3.connect(self.db_path) as con:
            # con.row_factory = sqlite3.Row
            cur = con.cursor()
            try:
                str_fac_id = '%' + str(fac_id) + '%'
                cur.execute("SELECT * FROM time_table WHERE faculty_id LIKE ?", (str_fac_id,))
                return cur
            except sqlite3.Error as e:
                return "Database error: %s" % e
            except Exception as e:
                return "Exception in _query: %s" % e
