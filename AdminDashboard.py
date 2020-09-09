import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtSql, QtPrintSupport

from StudentForm import StudentForm
from FacultyForm import FacultyForm
from ActivateUser import ActivateUser
from Views.AdminDashboard import Ui_dashboard


class AdminDashboard(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dashboard()
        self.ui.setupUi(self)

        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap("images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(window_icon)
        student_icon = QtGui.QIcon()
        student_icon.addPixmap(QtGui.QPixmap("images/student-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionStudent_2.setIcon(student_icon)
        faculty_icon = QtGui.QIcon()
        faculty_icon.addPixmap(QtGui.QPixmap("images/faculty-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionFaculty_2.setIcon(faculty_icon)
        exit_icon = QtGui.QIcon()
        exit_icon.addPixmap(QtGui.QPixmap("images/exit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionExit_toolbar.setIcon(exit_icon)
        activate_icon = QtGui.QIcon()
        activate_icon.addPixmap(QtGui.QPixmap("images/activate-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionActivateUser2.setIcon(activate_icon)

        self.student_form = StudentForm()
        self.ui.actionStudent.triggered.connect(self.show_student_form)
        self.ui.actionStudent_2.triggered.connect(self.show_student_form)

        self.faculty_form = FacultyForm()
        self.ui.actionFaculty.triggered.connect(self.show_faculty_form)
        self.ui.actionFaculty_2.triggered.connect(self.show_faculty_form)

        # new strategy comes in
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('Modals/TMS.db')
        self.model = QtSql.QSqlTableModel()
        self.delrow = -1
        self.initialize_table_modal(self.model)
        self.view1 = self.createView("Table Model (View 1)", self.model)
        self.view1.clicked.connect(self.findrow)
        layout = QVBoxLayout()
        layout.addWidget(self.view1)
        self.del_row_btn = QPushButton("Delete Student Data")
        self.add_row_btn = QPushButton("Add a row")
        btn_group = QHBoxLayout()
        # btn_group.addWidget(self.add_row_btn)
        btn_group.addWidget(self.del_row_btn)
        layout.addLayout(btn_group)
        self.add_row_btn.clicked.connect(self.add_row)
        self.del_row_btn.clicked.connect(self.remove_row)
        self.ui.studentTableView.setLayout(layout)

        self.faculty_model = QtSql.QSqlTableModel()
        self.delrow = -1
        self.initialize_faculty_table_modal(self.faculty_model)
        self.view2 = self.createView("Table Model (View 2)", self.faculty_model)
        self.view2.clicked.connect(self.findrow)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.view2)
        self.del_row_btn2 = QPushButton("Delete Faculty Data")
        self.add_row_btn2 = QPushButton("Add a row")
        btn_group2 = QHBoxLayout()
        # btn_group2.addWidget(self.add_row_btn2)
        btn_group2.addWidget(self.del_row_btn2)
        layout2.addLayout(btn_group2)
        self.add_row_btn2.clicked.connect(self.add_row2)
        self.del_row_btn2.clicked.connect(self.remove_row2)
        self.ui.facultyTableView.setLayout(layout2)

        self.time_table_model = QtSql.QSqlTableModel()
        self.delrow = -1
        self.initialize_time_table_modal(self.time_table_model)
        self.view3 = self.createView("Time Model (View 3)", self.time_table_model)
        self.view3.clicked.connect(self.findrow)
        layout3 = QVBoxLayout()
        layout3.addWidget(self.view3)
        self.del_row_btn3 = QPushButton("Delete Course")
        self.add_row_btn3 = QPushButton("Add a Course")
        btn_group3 = QHBoxLayout()
        btn_group3.addWidget(self.add_row_btn3)
        btn_group3.addWidget(self.del_row_btn3)
        layout3.addLayout(btn_group3)
        self.add_row_btn3.clicked.connect(self.add_row3)
        self.del_row_btn3.clicked.connect(self.remove_row3)
        self.ui.timeTableView.setLayout(layout3)

        print_icon = QtGui.QIcon()
        print_icon.addPixmap(QtGui.QPixmap("images/print-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.printStudents.setIcon(print_icon)
        self.ui.printFaculty.setIcon(print_icon)
        self.ui.printTimeTablebtn.setIcon(print_icon)

        self.ui.printStudents.clicked.connect(self.print_students)
        self.ui.printFaculty.clicked.connect(self.print_faculty)
        self.ui.printTimeTablebtn.clicked.connect(self.print_faculty)

        self.ui.actionActivateUser.triggered.connect(self.activate_new_user)
        self.ui.actionActivateUser2.triggered.connect(self.activate_new_user)

        logout_icon = QtGui.QIcon()
        logout_icon.addPixmap(QtGui.QPixmap("images/logout-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.actionLogout.setIcon(logout_icon)
        self.ui.actionLogout.triggered.connect(self.logout_user)

    def show_student_form(self):
        self.student_form.exec_()
        print('student form closing')
        # self.initialize_table_modal(self.model)
        self.model.select()
        print('table should be updated')

    def show_faculty_form(self):
        self.faculty_form.exec_()
        # self.initialize_faculty_table_modal(self.faculty_model)
        self.faculty_model.select()

    @staticmethod
    def initialize_table_modal(model):
        model.setTable('students')
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Age")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Address")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Gender")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Course")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Time_slot")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Facilities")

    @staticmethod
    def initialize_faculty_table_modal(model):
        model.setTable('faculty')
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Age")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Address")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Gender")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Course")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Qualification")

    @staticmethod
    def initialize_time_table_modal(model):
        model.setTable('time_table')
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Course Name")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Time Slot")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Week Day")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Faculty ID")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Student ID")

    def createView(self, title, model):
        view = QTableView()
        view.setModel(model)
        view.setWindowTitle(title)
        return view

    def add_row(self):
        print(self.model.rowCount())
        ret = self.model.insertRows(self.model.rowCount(), 1)
        print(ret)

    def add_row2(self):
        print(self.faculty_model.rowCount())
        ret = self.faculty_model.insertRows(self.faculty_model.rowCount(), 1)
        print(ret)

    def add_row3(self):
        print(self.time_table_model.rowCount())
        ret = self.time_table_model.insertRows(self.time_table_model.rowCount(), 1)
        print(ret)

    def remove_row(self):
        self.model.removeRow(self.view1.currentIndex().row())
        self.initialize_table_modal(self.model)

    def remove_row2(self):
        self.faculty_model.removeRow(self.view2.currentIndex().row())
        self.initialize_faculty_table_modal(self.faculty_model)

    def remove_row3(self):
        self.time_table_model.removeRow(self.view1.currentIndex().row())
        self.time_table_model(self.model)

    def findrow(self, i):
        delrow = i.row()

    def print_students(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.ui.studentTableView.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

    def print_faculty(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.ui.facultyTableView.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

    def print_time_table(self):
        printer = QtPrintSupport.QPrinter()
        painter = QtGui.QPainter()
        painter.begin(printer)
        screen = self.ui.timeTableView.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

    def activate_new_user(self):
        self.activate_user = ActivateUser()
        self.activate_user.exec_()

    def logout_user(self):
        self.destroy()
        import LoginForm
        self.login = LoginForm.Login()
        self.login.show()

#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myDashboard = AdminDashboard()
#     myDashboard.show()
#     sys.exit(app.exec_())
