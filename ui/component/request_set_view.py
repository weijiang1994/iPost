# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'request_set_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ssl_checkBox = QtWidgets.QCheckBox(Form)
        self.ssl_checkBox.setMinimumSize(QtCore.QSize(90, 0))
        self.ssl_checkBox.setChecked(True)
        self.ssl_checkBox.setObjectName("ssl_checkBox")
        self.horizontalLayout.addWidget(self.ssl_checkBox)
        self.horizontalLayout.setStretch(0, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.redirect_checkBox = QtWidgets.QCheckBox(Form)
        self.redirect_checkBox.setMinimumSize(QtCore.QSize(90, 0))
        self.redirect_checkBox.setChecked(True)
        self.redirect_checkBox.setObjectName("redirect_checkBox")
        self.horizontalLayout_5.addWidget(self.redirect_checkBox)
        self.horizontalLayout_5.setStretch(0, 10)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.conn_timeout_lineEdit = QtWidgets.QLineEdit(Form)
        self.conn_timeout_lineEdit.setMinimumSize(QtCore.QSize(90, 0))
        self.conn_timeout_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.conn_timeout_lineEdit.setObjectName("conn_timeout_lineEdit")
        self.horizontalLayout_3.addWidget(self.conn_timeout_lineEdit)
        self.horizontalLayout_3.setStretch(0, 10)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.read_timeout_lineEdit = QtWidgets.QLineEdit(Form)
        self.read_timeout_lineEdit.setMinimumSize(QtCore.QSize(90, 0))
        self.read_timeout_lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.read_timeout_lineEdit.setObjectName("read_timeout_lineEdit")
        self.horizontalLayout_4.addWidget(self.read_timeout_lineEdit)
        self.horizontalLayout_4.setStretch(0, 10)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enable SSL certificate verification"))
        self.ssl_checkBox.setText(_translate("Form", "ON"))
        self.label_5.setText(_translate("Form", "Automatically follow redirects"))
        self.redirect_checkBox.setText(_translate("Form", "ON"))
        self.label_3.setText(_translate("Form", "Connect Timeout"))
        self.label_4.setText(_translate("Form", "ReadTimeout"))
