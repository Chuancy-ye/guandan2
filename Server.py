from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QLabel,QFileDialog,QMainWindow,QMessageBox,QDesktopWidget,QAction,qApp,QTableWidgetItem
from PyQt5 import QtGui, QtCore

import guandan
from import_table import Ui_name
from check_table import Ui_ckName
class importName(QWidget):

    def __init__(self):
        super().__init__()
        self.ui2 = QWidget()
        self.tablename = Ui_name()
        self.tablename.setupUi(self.ui2)
        self.tablename.commandLinkButton.clicked.connect(self.importXls)
        self.tablename.pushButton_2.clicked.connect(self.saveName)
        self.ui2.show()

    def importXls(self):
        excel = QFileDialog.getOpenFileName(self, 'Open', '/home')
        if excel[0]:
            data = guandan.import_xl(excel[0])

            is4 = len(data) % 4

            # 分解列表为数组，人数必须是4的倍数才能玩
            list4c = []
            if is4 == 0:
                row = int(len(data) / 4)
                self.tablename.tableWidget.setRowCount(row)
                for i in range(0, row):
                    for j in range(0, 4):
                        #保存为4*n的数组，但是没必要
                        # if j == 0:
                        #     list4c.append([])
                        # list4c[i].append(data[j + i * 4])
                        # print(data[j + i * 4])
                        #以4列，row行显示
                        name = QTableWidgetItem(str(data[j + i * 4]))
                        self.tablename.tableWidget.setItem(i, j, name)
            else:
                print("参赛人员必须是4的倍数。")
    def saveJson(self):
        listname= {}
        row=self.tablename.tableWidget.rowCount()
        for i in range(0,row):
           for j in range(0,4):
            name=self.tablename.tableWidget.item(i,j).text()
            if name:
                data={ j + i * 4: name}
                listname.update(data)

        guandan.writeJson('name',listname)

    def saveName(self):

        reply = QMessageBox.question(self, '注意',
                                     "确定检查好了吗", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.saveJson()
            self.ui2.close()
class checkName(QWidget):
    def __init__(self):
        super(checkName, self).__init__()
        self.ui3 = QWidget()
        self.table = Ui_ckName()
        self.table.setupUi(self.ui3)
        self.readname()
        self.table.commandLinkButton.clicked.connect(self.importXls)
        self.table.pushButton_2.clicked.connect(self.saveName)
        self.ui3.show()
        # self.checkBox = QtWidgets.QCheckBox()
        # self.checkBox.setGeometry(QtCore.QRect(570, 110, 91, 19))
        # self.checkBox.setObjectName("checkBox")
    def readname(self):
        path='name'
        dicname=guandan.readJson(path)

        row = int(len(dicname) / 4)
        self.table.tableWidget.setRowCount(row)
        for i in range(0, row):
            print(i)
            for j in range(0, 4):
                # 保存为4*n的数组，但是没必要
                # if j == 0:
                #     list4c.append([])
                # list4c[i].append(data[j + i * 4])
                name=(dicname.get(str(j + i * 4)))

                # 以4列，row行显示
                name = QTableWidgetItem(name)
                self.table.tableWidget.setItem(i, j, name)

    def saveJson(self):
        listname = {}
        row = self.tablename.tableWidget.rowCount()
        for i in range(0, row):
            for j in range(0, 4):
                name = self.tablename.tableWidget.item(i, j).text()
                if name:
                    data = {j + i * 4: name}
                    listname.update(data)

        guandan.writeJson('name', listname)

    def importXls(self):
        excel = QFileDialog.getOpenFileName(self, 'Open', '/home')
        if excel[0]:
            data = guandan.import_xl(excel[0])

            is4 = len(data) % 4

            # 分解列表为数组，人数必须是4的倍数才能玩
            list4c = []
            if is4 == 0:
                row = int(len(data) / 4)
                self.tablename.tableWidget.setRowCount(row)
                for i in range(0, row):
                    for j in range(0, 4):
                        #保存为4*n的数组，但是没必要
                        # if j == 0:
                        #     list4c.append([])
                        # list4c[i].append(data[j + i * 4])
                        # print(data[j + i * 4])
                        #以4列，row行显示
                        name = QTableWidgetItem(str(data[j + i * 4]))
                        self.tablename.tableWidget.setItem(i, j, name)
            else:
                print("参赛人员必须是4的倍数。")

    def saveName(self):

        reply = QMessageBox.question(self, '注意',
                                     "确定检查好了吗", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.saveJson()
            self.ui2.close()


            # for i in range(0, 4):
        #     filename = QFileDialog.getSaveFileName(self, 'save file', '/home/jm/study')
        #     with open(filename[0], 'w') as f:
        #         my_text = self.textEdit.toPlainText()
        #         f.write(my_text)
            # for i in range(0,len(list4c)):
            #     for j in range(0,)

