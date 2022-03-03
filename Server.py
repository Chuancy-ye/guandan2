from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QLabel,QFileDialog,QMainWindow,QAbstractItemView,QMessageBox,QDesktopWidget,QAction,qApp,QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush,QColor,QFont
import guandan
from import_table import Ui_name
from check_table import Ui_ckName
class action(QWidget):
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
                        # 保存为4*n的数组，但是没必要
                        # if j == 0:
                        #     list4c.append([])
                        # list4c[i].append(data[j + i * 4])
                        # print(data[j + i * 4])
                        # 以4列，row行显示
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


class importName(action):

    def __init__(self):
        super(importName, self).__init__()
        self.ui2 = QWidget()
        self.tablename = Ui_name()
        self.tablename.setupUi(self.ui2)
        self.tablename.commandLinkButton.clicked.connect(self.importXls)
        self.tablename.pushButton_2.clicked.connect(self.saveName)
        self.ui2.show()


class checkName(action):
    def __init__(self):
        super(checkName, self).__init__()
        self.ui3 = QWidget()
        self.tablename = Ui_ckName()
        self.tablename.setupUi(self.ui3)
        self.readname()
        self.tablename.commandLinkButton.clicked.connect(self.importXls)
        self.tablename.pushButton_2.clicked.connect(self.saveName)
        self.tablename.checkBox.clicked.connect(self.can_change)


        self.ui3.show()
        # self.checkBox = QtWidgets.QCheckBox()
        # self.checkBox.setGeometry(QtCore.QRect(570, 110, 91, 19))
        # self.checkBox.setObjectName("checkBox")
    def can_change(self):
        check = self.tablename.checkBox.isChecked()
        if check:
            self.tablename.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        else:
            self.tablename.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def readname(self):
        path='name'
        dicname=guandan.readJson(path)

        row = int(len(dicname) / 4)
        self.tablename.tableWidget.setRowCount(row)
        for i in range(0, row):

            for j in range(0, 4):
                # 保存为4*n的数组，但是没必要
                # if j == 0:
                #     list4c.append([])
                # list4c[i].append(data[j + i * 4])
                name=(dicname.get(str(j + i * 4)))

                # 以4列，row行显示
                name = QTableWidgetItem(name)
                self.tablename.tableWidget.setItem(i, j, name)
        self.tablename.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def saveName(self):

        reply = QMessageBox.question(self, '注意',
                                     "确定检查好了吗", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.saveJson()
            self.ui3.close()
            # for i in range(0, 4):
        #     filename = QFileDialog.getSaveFileName(self, 'save file', '/home/jm/study')
        #     with open(filename[0], 'w') as f:
        #         my_text = self.textEdit.toPlainText()
        #         f.write(my_text)
            # for i in range(0,len(list4c)):
            #     for j in range(0,)
class deskPosition(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('座位图')
        self.show()
    def paintEvent(self,dp):
        #为什么会执行两次？可能和按钮有关
        dp = QPainter()
        dp.begin(self)
        self.drawDesk(dp)
        dp.end()

    def drawDesk(self,dp):
        self.setGeometry(500,500,900,700)
        c=200
        k=136

        record=guandan.readJson("sg")
        group=record.get('total')
        #n是比赛场次
        n=0
        #获取本场比赛的名单
        this_group=group[n]
        count_desk = len(this_group)/2
        if count_desk%3 == 0:
            row= int(count_desk/3)
        else:
            row = int(count_desk/3)+1

        for j in range(1,row+1):
            for i in range(1,4):
                desknumber = (j - 1) * 3 + i
                #判断桌子的个数，以免读多了报错
                if desknumber <= count_desk:
                    dp.setPen(QColor(168, 34, 3))
                    dp.setFont(QFont('Decorative', 25))
                    dp.drawRect(i*260-180, j*200-100, c, k)

                    name1=name2=name3=name4='空'
                    dicname= guandan.readJson('name')

                    for n in range(desknumber*2-1,desknumber*2+1):

                        if n%2==0:
                            name3 =dicname.get(str(this_group[n-1][0]))
                            name4 =dicname.get(str(this_group[n-1][1]))
                        else:
                            name1=dicname.get(str(this_group[n-1][0]))
                            name2=dicname.get(str(this_group[n-1][1]))

                    dp.drawText(i*260-140,j*200-15, '第'+str(desknumber)+'桌')
                    dp.setPen(QColor('bule'))
                    dp.setFont(QFont('Decorative', 16))
                    #桌子的位置比较难调整
                    dp.drawText(i*260-180,j*200-120, str(name1))
                    dp.drawText(i * 260-60, j * 200 - 120, str(name4))
                    dp.drawText(i * 260 - 60, j * 200+80, str(name2))
                    dp.drawText(i * 260 - 180, j * 200 + 80, str(name3))

