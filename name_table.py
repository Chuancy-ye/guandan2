# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'name_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_name(object):
    def setupUi(self, name):
        name.setObjectName("name")
        name.resize(820, 397)
        self.tableWidget = QtWidgets.QTableWidget(name)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 531, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_2 = QtWidgets.QPushButton(name)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 330, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(name)
        self.commandLinkButton.setGeometry(QtCore.QRect(561, 47, 201, 51))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(name)
        QtCore.QMetaObject.connectSlotsByName(name)

    def retranslateUi(self, name):
        _translate = QtCore.QCoreApplication.translate
        name.setWindowTitle(_translate("name", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("name", "A"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("name", "B"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("name", "C"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("name", "D"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("name", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("name", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("name", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("name", "4"))
        self.pushButton_2.setText(_translate("name", "确定"))
        self.commandLinkButton.setText(_translate("name", "导入"))
