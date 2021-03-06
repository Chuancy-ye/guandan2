import sys
import qtui
import os
from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QLabel,QFileDialog,QMainWindow,QMessageBox,QDesktopWidget,QAction,qApp,QTableWidgetItem
from PyQt5 import QtGui, QtCore
from table import Example
from import_table import Ui_name
import Server
import guandan
from Server import importName,checkName,deskPosition
class Guandan(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = qtui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.menu()
        self.statusBar().showMessage('Ready')
        self.center()
        self.En_buttton()
        self.ui.pushButton.clicked.connect(self.deakPosition)
        self.ui.pushButton.setStatusTip('查看座位分布')
        self.ui.pushButton_4.clicked.connect(self.chouqian)
        self.ui.pushButton_4.setStatusTip('换一组比赛组队')
        self.setWindowTitle('掼蛋神器')
        self.show()
    def En_menu(self):
        try:
            f = open('name')
            self.ui.menubar.actions()
            f.close()
        except IOError:
            print("File is not accessible.")
    def En_buttton(self):
        row=self.ui.tableWidget.rowCount()
        print(row)
        if row == 0:
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
        try:
            f = open('sg')
            self.ui.pushButton_6.setEnabled(True)
            f.close()
        except IOError:
            print("File is not accessible.")

    def menu(self):
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        about = QAction('&About',self)
        about.setShortcut('Ctrl+A')
        about.triggered.connect(self.about)
        
        # openFile = QAction('Open', self)
        # openFile.setShortcut('Ctrl+O')
        # openFile.setStatusTip('Open new File')
        # openFile.triggered.connect(self.Import_Xls)

        importName =QAction('添加',self)
        importName.setShortcut('Ctrl+i')
        importName.setStatusTip('从excel导入名单')
        importName.triggered.connect(self.importName)

        checkName = QAction('查看', self)
        checkName.setShortcut('Ctrl+c')
        checkName.setStatusTip('查看或修改参赛人员')
        checkName.triggered.connect(self.checkName)

        menubar= self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(about)
        fileMenu = menubar.addMenu('&参赛人员')
        fileMenu.addAction(importName)
        fileMenu.addAction(checkName)
        fileMenu=menubar.addAction(importName)

    def importName(self):
        self.name=importName()
        self.En_buttton()
    def checkName(self):
        self.name=checkName()
    def deakPosition(self):
        self.name =deskPosition()
    def chouqian(self):
        path = 'name'
        dicname = guandan.readJson(path)
        lenname = len(dicname)
        numList = list(range(0,lenname))
        grouppool = guandan.parter(numList)
        num1=len(grouppool)
        total=guandan.main(numList)

        row =len(total[0])

        self.ui.tableWidget.setRowCount(row)
        for i in range(0,len(total[0])):

            for j in range(0,2):
              namenum=total[0][i][j]
              dicname=guandan.readJson('name')
              name = dicname.get(str(namenum))
              name = QTableWidgetItem(str(name))
              self.ui.tableWidget.setItem(i,j,name)

        num2 = len(total)
        record = {'groupool':grouppool,'num':1,'total':total}
        self.ui.textBrowser.setText(
            "共有"+str(num1)+"种组队方式，"+"可以比赛"+str(num2)+"次。"+"\n详情请点击组队池"
        )
        guandan.writeJson('sg',record)
        self.En_buttton()
    def about(self):
        msg = "作者：叶祥鹰" "\n中科大东区理化大楼" "\n\n邮箱：1982919845@qq.com" "\n更多开源：www.github.com/Chuancy-Ye"
        reply = QMessageBox.information(self, '欢迎使用', msg, QMessageBox.Ok, QMessageBox.Help
                                        )
        if reply == QMessageBox.Help:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.github.com/Chuancy-Ye/guandan2'))


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Guandan()
    sys.exit(app.exec_())