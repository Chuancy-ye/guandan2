import sys
import qtui
from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QLabel,QMainWindow,QMessageBox,QDesktopWidget,QAction,qApp
from PyQt5 import QtGui, QtCore

class Example(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = qtui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def menu(self):
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)
        about = QAction('&About',self)
        about.setShortcut('Ctrl+A')
        about.triggered.connect(self.about)
        menubar= self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(about)
    def about(self):
        msg = "作者：叶祥鹰" "\n中科大东区理化大楼" "\n\n邮箱：1982919845@qq.com" "\n更多开源：www.github.com/Chuancy-Ye"
        reply= QMessageBox.information(self, '欢迎使用',msg,QMessageBox.Ok, QMessageBox.Help
                                )
        if reply==QMessageBox.Help:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl('www.github.com/Chuancy-Ye/guandan2'))


    def initUI(self):
        self.menu()
        self.statusBar().showMessage('Ready')
        self.center()
        self.setWindowTitle('Message box')
        self.show()

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
    ex = Example()

    sys.exit(app.exec_())