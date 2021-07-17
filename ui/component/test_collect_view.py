# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_collect_view.ui'
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
        self.test_collect_treeWidget = QtWidgets.QTreeWidget(Form)
        self.test_collect_treeWidget.setObjectName("test_collect_treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.test_collect_treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.test_collect_treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.test_collect_treeWidget)
        self.gridLayout.addWidget(self.test_collect_treeWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.test_collect_treeWidget.headerItem().setText(0, _translate("Form", "test"))
        __sortingEnabled = self.test_collect_treeWidget.isSortingEnabled()
        self.test_collect_treeWidget.setSortingEnabled(False)
        self.test_collect_treeWidget.topLevelItem(0).setText(0, _translate("Form", "auth/api_key"))
        self.test_collect_treeWidget.topLevelItem(1).setText(0, _translate("Form", "auth/api_key"))
        self.test_collect_treeWidget.topLevelItem(2).setText(0, _translate("Form", "auth/api_key"))
        self.test_collect_treeWidget.setSortingEnabled(__sortingEnabled)
