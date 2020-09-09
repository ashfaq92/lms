import sys
import sqlite3
from PyQt5.QtWidgets import *

from Modals.UsersModal import UsersModal
from Modals.StudentsModal import StudentsModal
from Modals.FacultyModal import FacultyModal
from Views.ActivateUser import Ui_ActivateUser


class ActivateUser(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ActivateUser()
        self.ui.setupUi(self)
        self.ui.activateButton.clicked.connect(self.send_data)

    def send_data(self):
        user_data = {
            'type': self.ui.userType.currentText(),
            'id': int(self.ui.userIdLineEdit.text()),
            'email': self.ui.emailLineEdit.text(),
            'login_id': self.ui.loginIdLineEdit.text(),
            'password': self.ui.passwordLineEdit.text(),
        }
        if user_data['type'] == 'Student':
            students_table = StudentsModal()
            results = students_table.find_stud_by_id(user_data['id'])
            if results.fetchone():
                users_table = UsersModal()
                resp = users_table.insert_user(user_data)
                # resp2 = students_table.insert_student()
                if resp != -1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Response')
                    msg.setText(
                        'Student Activated Successfully. Login_id: ' + user_data['login_id'] + ' Password: ' + user_data[
                            'password'])
                    msg.exec_()
                    self.close()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Response')
                msg.setText('Could not find student. Recheck Student ID!')
                msg.exec_()

        elif user_data['type'] == 'Faculty':
            faculty_table = FacultyModal()
            results = faculty_table.find_faculty_by_id(user_data['id'])
            if results.fetchone():
                users_table = UsersModal()
                resp = users_table.insert_user(user_data)
                if resp != -1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Response')
                    msg.setText(
                        'Faculty Activated Successfully. Now he can login with id: ' + user_data['login_id'] + ' and Password: ' + user_data['password'])
                    msg.exec_()
                    self.close()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Response')
                msg.setText('Could not find Faculty. Recheck Faculty ID!')
                msg.exec_()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myFacultyForm = ActivateUser()
#     myFacultyForm.show()
#     sys.exit(app.exec_())
