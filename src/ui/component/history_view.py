# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.search_key_lineEdit = QtWidgets.QLineEdit(Form)
        self.search_key_lineEdit.setObjectName("search_key_lineEdit")
        self.gridLayout.addWidget(self.search_key_lineEdit, 0, 0, 1, 1)
        self.history_treeWidget = QtWidgets.QTreeWidget(Form)
        self.history_treeWidget.setObjectName("history_treeWidget")
        self.gridLayout.addWidget(self.history_treeWidget, 2, 0, 1, 1)
        self.hint_label = QtWidgets.QLabel(Form)
        self.hint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_label.setObjectName("hint_label")
        self.gridLayout.addWidget(self.hint_label, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hint_label.setText(_translate("Form", "TextLabel"))
