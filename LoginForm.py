import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

from AdminDashboard import AdminDashboard
from FacultyDashboard import FacultyDashboard
from StudentDashboard import StudentDashboard
from Modals.UsersModal import *
from Views.LoginForm import Ui_LoginForm


class Login(QDialog):
    tries_limit = 2
    tries = 0

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.show()
        self.ui.login_btn.clicked.connect(self.check_login)
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(window_icon)

        banner = QtGui.QPixmap("images/university-banner.png")
        self.ui.universityBanner.setPixmap(banner)
        self.user_table = UsersModal()
        print(self.user_table.base_dir)
        print(self.user_table.db_path)

    def check_login(self):
        login_id = self.ui.username_entry.text()
        password = self.ui.password_entry.text()
        row = self.user_table.check_user(login_id, password)
        if self.tries < self.tries_limit:
            if row == 'Wrong Password':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Response')
                msg.setText('Wrong Password. Tries Remaining: ' + str(self.tries_limit - self.tries))
                msg.exec_()
                self.ui.username_entry.setText('')
                self.ui.username_entry.setFocus()
                self.ui.password_entry.setText('')
                self.tries += 1
            elif row == 'Invalid Login':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Response')
                msg.setText('Invalid Login Details. Tries Remaining: ' + str(self.tries_limit - self.tries))
                msg.exec_()
                self.ui.username_entry.setText('')
                self.ui.username_entry.setFocus()
                self.ui.password_entry.setText('')
                self.tries += 1
            elif row['type'] == 'admin':
                self.destroy()
                self.admin_dashboard = AdminDashboard()
                self.admin_dashboard.show()
            elif row['type'] == 'Student':
                self.destroy()
                self.student_dashboard = StudentDashboard(row)
                self.student_dashboard.show()
            elif row['type'] == 'Faculty':
                self.destroy()
                self.faculty_dashboard = FacultyDashboard(row)
                self.faculty_dashboard.show()
            else:
                print('unknown error in checking login')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error')
            msg.setText('Number of tries limit exceeded. System is going to quit')
            msg.exec_()
            self.destroy()


def main():
    app = QApplication(sys.argv)
    myLogin = Login()
    myLogin.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()
