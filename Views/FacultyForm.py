# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designs/FacultyForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FacultyDetails(object):
    def setupUi(self, FacultyDetails):
        FacultyDetails.setObjectName("FacultyDetails")
        FacultyDetails.resize(601, 657)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        FacultyDetails.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(FacultyDetails)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 60, 311, 562))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.ageLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ageLabel)
        self.ageSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ageSpinBox.setFont(font)
        self.ageSpinBox.setObjectName("ageSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ageSpinBox)
        self.addressLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.addressTextEdit.setFont(font)
        self.addressTextEdit.setObjectName("addressTextEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addressTextEdit)
        self.genderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.maleRadioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maleRadioButton.sizePolicy().hasHeightForWidth())
        self.maleRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.maleRadioButton.setFont(font)
        self.maleRadioButton.setIconSize(QtCore.QSize(15, 16))
        self.maleRadioButton.setObjectName("maleRadioButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(FacultyDetails)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.maleRadioButton)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.maleRadioButton)
        self.femaleRadioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.femaleRadioButton.setFont(font)
        self.femaleRadioButton.setObjectName("femaleRadioButton")
        self.buttonGroup_2.addButton(self.femaleRadioButton)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.femaleRadioButton)
        self.courseLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.courseLabel.setFont(font)
        self.courseLabel.setObjectName("courseLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.courseLabel)
        self.courseList = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.courseList.setFont(font)
        self.courseList.setObjectName("courseList")
        self.courseList.addItem("")
        self.courseList.addItem("")
        self.courseList.addItem("")
        self.courseList.addItem("")
        self.courseList.addItem("")
        self.courseList.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.courseList)
        self.timeSlotLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.timeSlotLabel.setFont(font)
        self.timeSlotLabel.setObjectName("timeSlotLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.timeSlotLabel)
        self.qualification = QtWidgets.QListWidget(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.qualification.setFont(font)
        self.qualification.setObjectName("qualification")
        item = QtWidgets.QListWidgetItem()
        self.qualification.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.qualification.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.qualification.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.qualification.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.qualification.addItem(item)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.qualification)
        self.okButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.okButton.setObjectName("okButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.okButton)
        self.closeButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.closeButton)
        self.label = QtWidgets.QLabel(FacultyDetails)
        self.label.setGeometry(QtCore.QRect(130, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.uploadPicBtn = QtWidgets.QPushButton(FacultyDetails)
        self.uploadPicBtn.setGeometry(QtCore.QRect(410, 60, 81, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.uploadPicBtn.setFont(font)
        self.uploadPicBtn.setObjectName("uploadPicBtn")
        self.picView = QtWidgets.QLabel(FacultyDetails)
        self.picView.setGeometry(QtCore.QRect(410, 100, 111, 122))
        self.picView.setText("")
        self.picView.setObjectName("picView")

        self.retranslateUi(FacultyDetails)
        self.qualification.setCurrentRow(-1)
        self.closeButton.clicked.connect(FacultyDetails.close)
        QtCore.QMetaObject.connectSlotsByName(FacultyDetails)

    def retranslateUi(self, FacultyDetails):
        _translate = QtCore.QCoreApplication.translate
        FacultyDetails.setWindowTitle(_translate("FacultyDetails", "Faculty Data"))
        self.nameLabel.setText(_translate("FacultyDetails", "Name"))
        self.ageLabel.setText(_translate("FacultyDetails", "Age"))
        self.addressLabel.setText(_translate("FacultyDetails", "Address"))
        self.genderLabel.setText(_translate("FacultyDetails", "Gender"))
        self.maleRadioButton.setText(_translate("FacultyDetails", "Male"))
        self.femaleRadioButton.setText(_translate("FacultyDetails", "Female"))
        self.courseLabel.setText(_translate("FacultyDetails", "Course"))
        self.courseList.setItemText(0, _translate("FacultyDetails", "----------Select-------"))
        self.courseList.setItemText(1, _translate("FacultyDetails", "Software Engineering"))
        self.courseList.setItemText(2, _translate("FacultyDetails", "Software Systems Design"))
        self.courseList.setItemText(3, _translate("FacultyDetails", "Software Testing"))
        self.courseList.setItemText(4, _translate("FacultyDetails", "Java Development"))
        self.courseList.setItemText(5, _translate("FacultyDetails", "Web Development"))
        self.timeSlotLabel.setText(_translate("FacultyDetails", "Qualification"))
        self.qualification.setSortingEnabled(False)
        __sortingEnabled = self.qualification.isSortingEnabled()
        self.qualification.setSortingEnabled(False)
        item = self.qualification.item(0)
        item.setText(_translate("FacultyDetails", "GNNIT/DNNIT"))
        item = self.qualification.item(1)
        item.setText(_translate("FacultyDetails", "MCA"))
        item = self.qualification.item(2)
        item.setText(_translate("FacultyDetails", "B.E."))
        item = self.qualification.item(3)
        item.setText(_translate("FacultyDetails", "MCAD/MCSD"))
        item = self.qualification.item(4)
        item.setText(_translate("FacultyDetails", "CCNA"))
        self.qualification.setSortingEnabled(__sortingEnabled)
        self.okButton.setText(_translate("FacultyDetails", "OK"))
        self.closeButton.setText(_translate("FacultyDetails", "Close"))
        self.label.setText(_translate("FacultyDetails", "Accept Faculty Data"))
        self.uploadPicBtn.setText(_translate("FacultyDetails", "Upload Picture"))


