# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'api_view.ui'
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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.api_url_lineEdit = QtWidgets.QLineEdit(Form)
        self.api_url_lineEdit.setObjectName("api_url_lineEdit")
        self.horizontalLayout.addWidget(self.api_url_lineEdit)
        self.send_pushButton = QtWidgets.QPushButton(Form)
        self.send_pushButton.setObjectName("send_pushButton")
        self.horizontalLayout.addWidget(self.send_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "GET"))
        self.comboBox.setItemText(1, _translate("Form", "POST"))
        self.comboBox.setItemText(2, _translate("Form", "PUT"))
        self.comboBox.setItemText(3, _translate("Form", "DELETE"))
        self.api_url_lineEdit.setPlaceholderText(_translate("Form", "请输入API地址"))
        self.send_pushButton.setText(_translate("Form", "Send"))