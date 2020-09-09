import sys
import os

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Modals.StudentsModal import StudentsModal
from Views.StudentForm import Ui_StudentDetails


class StudentForm(QDialog):
    user_picture = None
    file_name = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_StudentDetails()
        self.ui.setupUi(self)
        # self.ui.okButton.clicked.connect(self.send_data)
        self.ui.okButton.clicked.connect(self.chk_validation)
        self.ui.uploadPicBtn.clicked.connect(self.open_image)

    def get_gender(self):
        if self.ui.maleRadioButton.isChecked():
            gender = self.ui.maleRadioButton.text()
        elif self.ui.femaleRadioButton.isChecked():
            gender = self.ui.maleRadioButton.text()
        else:
            gender = None
        return gender

    def get_facilities(self):
        facilities = ''
        if self.ui.libraryCheckBox.isChecked():
            facilities = self.ui.libraryCheckBox.text()
        if self.ui.computerCheckBox.isChecked():
            facilities += "," + self.ui.computerCheckBox.text()
        return facilities

    def chk_validation(self):
        if not self.ui.nameLineEdit.text():
            print('please enter name')
            self.ui.nameLineEdit.setStyleSheet(""".QLineEdit {border: 1px solid red;}""")
        elif not int(self.ui.ageSpinBox.text()):
            print('please enter age')
            self.ui.ageSpinBox.setStyleSheet(""".QSpinBox {border: 1px solid red;}""")
            self.ui.nameLineEdit.setStyleSheet("")
        elif not self.ui.addressTextEdit.toPlainText():
            print('please enter address')
            self.ui.addressTextEdit.setStyleSheet(""".QPlainTextEdit {border: 1px solid red;}""")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        elif not self.get_gender():
            print('please enter gender')
            self.ui.maleRadioButton.setStyleSheet(""".QRadioButton {border: 1px solid red;}""")
            self.ui.femaleRadioButton.setStyleSheet(""".QRadioButton {border: 1px solid red;}""")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        elif self.ui.courseList.currentText() == '----------Select-------':
            print('plese select course')
            self.ui.courseList.setStyleSheet(""".QComboBox {border: 1px solid red;}""")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        elif not self.get_facilities():
            print('please select facilities')
            self.ui.libraryCheckBox.setStyleSheet(""".QCheckBox {border: 1px solid red;}""")
            self.ui.computerCheckBox.setStyleSheet(""".QCheckBox {border: 1px solid red;}""")

            self.ui.courseList.setStyleSheet("")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        elif not self.user_picture:
            print('please select picture')
            self.ui.uploadPicBtn.setStyleSheet(""".QPushButton {border: 1px solid red;}""")

            self.ui.libraryCheckBox.setStyleSheet("")
            self.ui.computerCheckBox.setStyleSheet("")
            self.ui.courseList.setStyleSheet("")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        else:
            print('All fields are filled')
            self.ui.uploadPicBtn.setStyleSheet("")
            self.ui.libraryCheckBox.setStyleSheet("")
            self.ui.computerCheckBox.setStyleSheet("")
            self.ui.courseList.setStyleSheet("")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")

            self.send_data()

    def send_data(self):
        student_data = {
            'name': self.ui.nameLineEdit.text(),
            'age': int(self.ui.ageSpinBox.text()),
            'address': self.ui.addressTextEdit.toPlainText(),
            'gender': self.get_gender(),
            'course': self.ui.courseList.currentText(),
            'time_slot': self.ui.timeSlot.currentItem().text(),
            'facilities': self.get_facilities(),
            'picture': self.user_picture
        }
        student_table = StudentsModal()
        resp = student_table.insert_student(student_data)
        if resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Response')
            msg.setText('Student Added Successfully')
            msg.exec_()
            self.close()

        else:
            QErrorMessage('Error in Adding Student')

    def open_image(self):
        try:
            self.file_name = QFileDialog.getOpenFileName(None, 'Select an Image', os.getenv('HOME'),
                                                         'Images (*.png *.jpg *.jpeg *.bmp *.gif)')
            if self.file_name:
                picture_original = QtGui.QPixmap(self.file_name[0])
                picture_resized = picture_original.scaledToWidth(111)
                picture_resized = picture_resized.scaledToHeight(121)
                self.ui.picView.setPixmap(picture_resized)

                self.user_picture = self.convertToBinaryData(self.file_name[0])
        except:
            print('QFileDialog Closed')

    def convertToBinaryData(self, filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myStudentForm = StudentForm()
#     myStudentForm.show()
#     sys.exit(app.exec_())
