# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hint_view.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.icon_label = QtWidgets.QLabel(Form)
        self.icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_label.setObjectName("icon_label")
        self.verticalLayout.addWidget(self.icon_label)
        self.hint_msg_label = QtWidgets.QLabel(Form)
        self.hint_msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_msg_label.setObjectName("hint_msg_label")
        self.verticalLayout.addWidget(self.hint_msg_label)
        self.detail_label = QtWidgets.QLabel(Form)
        self.detail_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detail_label.setObjectName("detail_label")
        self.verticalLayout.addWidget(self.detail_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.icon_label.setText(_translate("Form", "TextLabel"))
        self.hint_msg_label.setText(_translate("Form", "TextLabel"))
        self.detail_label.setText(_translate("Form", "TextLabel"))
