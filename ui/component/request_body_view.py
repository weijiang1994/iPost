# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'request_body_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.none_radioButton = QtWidgets.QRadioButton(Form)
        self.none_radioButton.setObjectName("none_radioButton")
        self.horizontalLayout.addWidget(self.none_radioButton)
        self.form_radioButton = QtWidgets.QRadioButton(Form)
        self.form_radioButton.setObjectName("form_radioButton")
        self.horizontalLayout.addWidget(self.form_radioButton)
        self.raw_radioButton = QtWidgets.QRadioButton(Form)
        self.raw_radioButton.setObjectName("raw_radioButton")
        self.horizontalLayout.addWidget(self.raw_radioButton)
        self.binary_radioButton = QtWidgets.QRadioButton(Form)
        self.binary_radioButton.setObjectName("binary_radioButton")
        self.horizontalLayout.addWidget(self.binary_radioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.body_stackedWidget = QtWidgets.QStackedWidget(Form)
        self.body_stackedWidget.setObjectName("body_stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.body_stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.body_stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.body_stackedWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.none_radioButton.setText(_translate("Form", "none"))
        self.form_radioButton.setText(_translate("Form", "form-data"))
        self.raw_radioButton.setText(_translate("Form", "raw"))
        self.binary_radioButton.setText(_translate("Form", "binary"))