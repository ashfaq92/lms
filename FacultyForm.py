import sys
import os
from PyQt5.QtWidgets import *

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Modals.FacultyModal import FacultyModal
from Views.FacultyForm import Ui_FacultyDetails


class FacultyForm(QDialog):
    user_picture = None
    file_name = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FacultyDetails()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(self.chk_validation)
        self.ui.uploadPicBtn.clicked.connect(self.open_image)

    def get_gender(self):
        if self.ui.maleRadioButton.isChecked():
            gender = self.ui.maleRadioButton.text()
        elif self.ui.femaleRadioButton.isChecked():
            gender = self.ui.maleRadioButton.text()
        else:
            gender = 'Error'
        return gender

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
        elif not self.ui.qualification:
            print('please select qualification')
            self.ui.qualification.setStyleSheet(""".QListWidget {border: 1px solid red;}""")

            self.ui.courseList.setStyleSheet("")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        elif not self.user_picture:
            print('please select picture')
            self.ui.uploadPicBtn.setStyleSheet(""".QPushButton {border: 1px solid red;}""")

            self.ui.qualification.setStyleSheet("")
            self.ui.courseList.setStyleSheet("")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")
        else:
            print('All fields are filled')
            self.ui.uploadPicBtn.setStyleSheet("")
            self.ui.qualification.setStyleSheet("")
            self.ui.courseList.setStyleSheet("")
            self.ui.maleRadioButton.setStyleSheet("")
            self.ui.femaleRadioButton.setStyleSheet("")
            self.ui.addressTextEdit.setStyleSheet("")
            self.ui.nameLineEdit.setStyleSheet("")
            self.ui.ageSpinBox.setStyleSheet("")

            self.send_data()

    def send_data(self):
        faculty_data = {
            'name': self.ui.nameLineEdit.text(),
            'age': int(self.ui.ageSpinBox.text()),
            'address': self.ui.addressTextEdit.toPlainText(),
            'gender': self.get_gender(),
            'course': self.ui.courseList.currentText(),
            'qualification': self.ui.qualification.currentItem().text(),
            'picture': self.user_picture

        }
        faculty_table = FacultyModal()
        resp = faculty_table.insert_faculty(faculty_data)
        if resp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Response')
            msg.setText('Faculty Added Successfully')
            msg.exec_()
            self.close()
        else:
            QErrorMessage('Error in Adding Faculty')

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
#     myFacultyForm = FacultyForm()
#     myFacultyForm.show()
#     sys.exit(app.exec_())
