import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtSql, QtPrintSupport

from Modals.StudentsModal import StudentsModal
from Modals.TimeTableModal import TimeTableModal
from Views.StudentDashboard import Ui_studentDashboard


class StudentDashboard(QMainWindow):
    def __init__(self, row=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_studentDashboard()
        self.ui.setupUi(self)
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(window_icon)

        details_icon = QtGui.QIcon()
        details_icon.addPixmap(QtGui.QPixmap("images/student-details-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionDetails.setIcon(details_icon)

        exit_icon = QtGui.QIcon()
        exit_icon.addPixmap(QtGui.QPixmap("images/exit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionExit_toolbar.setIcon(exit_icon)

        logout_icon = QtGui.QIcon()
        logout_icon.addPixmap(QtGui.QPixmap("images/logout-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionLogout.setIcon(logout_icon)
        self.ui.actionLogout.triggered.connect(self.logout_user)

        self.user = row  # Associated Array (dictionary) containing student login info
        student_table = StudentsModal()
        student_row = student_table.find_stud_by_id(self.user['parent_id'])  # Change this
        # student_row = student_table.find_stud_by_id(4347)  # Change this
        self.student = student_row.fetchone()  # Associated Array (Dictionary) contains student data

        self.ui.studentLabel.setText('Student Dashboard. Welcome ' + self.student['name'].title())
        self.populate_student_data()

        print_icon = QtGui.QIcon()
        print_icon.addPixmap(QtGui.QPixmap("images/print-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.printButton.setIcon(print_icon)
        self.ui.printButton_2.setIcon(print_icon)
        self.ui.printButton.clicked.connect(self.print_data)
        self.ui.printButton_2.clicked.connect(self.print_time_table)

        header = self.ui.timeTableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        self.show_time_table()

    def logout_user(self):
        self.destroy()
        import LoginForm
        self.login = LoginForm.Login()
        self.login.show()

    def populate_student_data(self):
        self.ui.label_2.setText(str(self.student['id']))
        self.ui.label_4.setText(self.student['name'])
        self.ui.label_6.setText(str(self.student['age']))
        self.ui.label_8.setText(self.student['address'])
        self.ui.label_9.setText(self.student['gender'])
        self.ui.label_12.setText(self.student['course'])
        self.ui.label_14.setText(self.student['time_slot'])
        self.ui.label_15.setText(self.student['facilities'])

        image_data = self.student['picture']
        qimg = QtGui.QImage.fromData(image_data)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        picture_resized = pixmap.scaledToWidth(111)
        picture_resized = picture_resized.scaledToHeight(121)
        self.ui.picView.setPixmap(picture_resized)

    def show_time_table(self):
        # self.ui.timeTableView.setItem(0, 0, QTableWidgetItem("dummy text"))
        time_table = TimeTableModal()
        time_table_data = time_table.get_time_table_by_student_id(self.user['parent_id'])
        time_table_records = time_table_data.fetchall()
        self.ui.timeTableView.setRowCount(len(time_table_records))

        sorted_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        time_table_records = sorted(time_table_records, key=lambda x: sorted_days.index(x[3]))
        # print(time_table_records)
        for row in range(0, len(time_table_records)):
            for col in range(0, 4):
                self.ui.timeTableView.setItem(row, col, QTableWidgetItem(str(time_table_records[row][col])))

    def print_data(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.ui.personalDetailsLabel.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

    def print_time_table(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.ui.timeTableView.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myDashboard = StudentDashboard()
#     myDashboard.show()
#     sys.exit(app.exec_())
