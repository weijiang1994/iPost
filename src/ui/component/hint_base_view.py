# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hint_base_view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(216, 80)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_pushButton = QtWidgets.QPushButton(Form)
        self.close_pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout.addWidget(self.close_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hint_icon_label = QtWidgets.QLabel(Form)
        self.hint_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_icon_label.setObjectName("hint_icon_label")
        self.horizontalLayout_2.addWidget(self.hint_icon_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hint_cate_label = QtWidgets.QLabel(Form)
        self.hint_cate_label.setObjectName("hint_cate_label")
        self.verticalLayout.addWidget(self.hint_cate_label)
        self.hint_msg_label = QtWidgets.QLabel(Form)
        self.hint_msg_label.setObjectName("hint_msg_label")
        self.verticalLayout.addWidget(self.hint_msg_label)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.close_pushButton.setText(_translate("Form", "×"))
        self.hint_icon_label.setText(_translate("Form", "提示图标"))
        self.hint_cate_label.setText(_translate("Form", "提示类别"))
        self.hint_msg_label.setText(_translate("Form", "提示内容"))
