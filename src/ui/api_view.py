# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'api_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(675, 600)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.send_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_pushButton.setObjectName("send_pushButton")
        self.horizontalLayout.addWidget(self.send_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.params_pushButton = QtWidgets.QPushButton(Form)
        self.params_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.params_pushButton.setObjectName("params_pushButton")
        self.horizontalLayout_2.addWidget(self.params_pushButton)
        self.headers_pushButton = QtWidgets.QPushButton(Form)
        self.headers_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.headers_pushButton.setObjectName("headers_pushButton")
        self.horizontalLayout_2.addWidget(self.headers_pushButton)
        self.body_pushButton = QtWidgets.QPushButton(Form)
        self.body_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.body_pushButton.setObjectName("body_pushButton")
        self.horizontalLayout_2.addWidget(self.body_pushButton)
        self.cookies_pushButton = QtWidgets.QPushButton(Form)
        self.cookies_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cookies_pushButton.setObjectName("cookies_pushButton")
        self.horizontalLayout_2.addWidget(self.cookies_pushButton)
        self.setting_pushButton = QtWidgets.QPushButton(Form)
        self.setting_pushButton.setObjectName("setting_pushButton")
        self.horizontalLayout_2.addWidget(self.setting_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.api_stackedWidget = QtWidgets.QStackedWidget(Form)
        self.api_stackedWidget.setMinimumSize(QtCore.QSize(0, 200))
        self.api_stackedWidget.setObjectName("api_stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.api_stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.api_stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.api_stackedWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.res_body_pushButton = QtWidgets.QPushButton(Form)
        self.res_body_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.res_body_pushButton.setObjectName("res_body_pushButton")
        self.horizontalLayout_3.addWidget(self.res_body_pushButton)
        self.res_cookies_pushButton = QtWidgets.QPushButton(Form)
        self.res_cookies_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.res_cookies_pushButton.setObjectName("res_cookies_pushButton")
        self.horizontalLayout_3.addWidget(self.res_cookies_pushButton)
        self.res_headers_pushButton = QtWidgets.QPushButton(Form)
        self.res_headers_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.res_headers_pushButton.setObjectName("res_headers_pushButton")
        self.horizontalLayout_3.addWidget(self.res_headers_pushButton)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.code_label = QtWidgets.QLabel(Form)
        self.code_label.setObjectName("code_label")
        self.horizontalLayout_4.addWidget(self.code_label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_4.addWidget(self.time_label)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.size_label = QtWidgets.QLabel(Form)
        self.size_label.setObjectName("size_label")
        self.horizontalLayout_4.addWidget(self.size_label)
        self.res_save_pushButton = QtWidgets.QPushButton(Form)
        self.res_save_pushButton.setObjectName("res_save_pushButton")
        self.horizontalLayout_4.addWidget(self.res_save_pushButton)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.res_stackedWidget = QtWidgets.QStackedWidget(Form)
        self.res_stackedWidget.setObjectName("res_stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.res_stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.res_stackedWidget.addWidget(self.page_4)
        self.verticalLayout_2.addWidget(self.res_stackedWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 10)

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
        self.params_pushButton.setText(_translate("Form", "Params"))
        self.headers_pushButton.setText(_translate("Form", "Headers"))
        self.body_pushButton.setText(_translate("Form", "Body"))
        self.cookies_pushButton.setText(_translate("Form", "Cookies"))
        self.setting_pushButton.setText(_translate("Form", "Setting"))
        self.res_body_pushButton.setText(_translate("Form", "Body"))
        self.res_cookies_pushButton.setText(_translate("Form", "Cookies"))
        self.res_headers_pushButton.setText(_translate("Form", "Headers"))
        self.label.setText(_translate("Form", "Status:"))
        self.code_label.setText(_translate("Form", "200"))
        self.label_2.setText(_translate("Form", "Time:"))
        self.time_label.setText(_translate("Form", "200"))
        self.label_3.setText(_translate("Form", "Size:"))
        self.size_label.setText(_translate("Form", "200"))
        self.res_save_pushButton.setText(_translate("Form", "Save"))