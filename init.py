import sys
import qtui
from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QLabel,QFileDialog,QMainWindow,QMessageBox,QDesktopWidget,QAction,qApp,QTableWidgetItem
from PyQt5 import QtGui, QtCore
from table import Example
from name_table import Ui_name
import guandan
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
        self.setWindowTitle('掼蛋神器')
        self.show()
        self.ui.pushButton.clicked.connect(self.name2)
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
        importName.triggered.connect(self.name2)

        menubar= self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(about)
        fileMenu = menubar.addMenu('&参赛人员')
        fileMenu.addAction(importName)

    def table(self):
        self.name = Example()


    def name2(self):
        self.ui2 = QWidget()
        self.name = Ui_name()
        self.name.setupUi(self.ui2)
        self.name.commandLinkButton.clicked.connect(self.importXls)
        self.ui2.show()



    def about(self):
        msg = "作者：叶祥鹰" "\n中科大东区理化大楼" "\n\n邮箱：1982919845@qq.com" "\n更多开源：www.github.com/Chuancy-Ye"
        reply= QMessageBox.information(self, '欢迎使用',msg,QMessageBox.Ok, QMessageBox.Help
                                )
        if reply==QMessageBox.Help:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.github.com/Chuancy-Ye/guandan2'))

    def importXls(self):
        excel = QFileDialog.getOpenFileName(self,'Open','/home')
        if excel[0]:
            # print(excel[0])
            # f= open(excel[0], 'r')
            # with f:
            #     data = f.read()
            #     print(data)
            #     self.ui.textEdit.setText(data)
            data = guandan.import_xl(excel[0])

            self.ui.textEdit.setText(str(data))
            is4 = len(data)%4

            #分解数组
            list4c=[]
            if is4 == 0:

                row = int(len(data)/4)
                for i in range(0,row):
                    for j in range(0,4):
                        if j == 0:
                            list4c.append([])
                        list4c[i].append(data[j+i*4])
                        print(data[j+i*4])
                        name = QTableWidgetItem(str(data[j+i*4]))
                        self.name.tableWidget.setItem(i, j, name)

            # for i in range(0,len(list4c)):
            #     for j in range(0,)
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