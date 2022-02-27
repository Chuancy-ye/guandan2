from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QLabel,QFileDialog,QMainWindow,QMessageBox,QDesktopWidget,QAction,qApp,QTableWidgetItem
from PyQt5 import QtGui, QtCore
import guandan
from name_table import Ui_name
class Server_table(QWidget):

    def __init__(self):
        super().__init__()
        self.ui2 = QWidget()
        self.tablename = Ui_name()
        self.tablename.setupUi(self.ui2)
        self.tablename.commandLinkButton.clicked.connect(self.importXls)
        self.ui2.show()

    def importXls(self):
        excel = QFileDialog.getOpenFileName(self, 'Open', '/home')
        if excel[0]:
            data = guandan.import_xl(excel[0])

            is4 = len(data) % 4

            # 分解数组
            list4c = []
            if is4 == 0:
                row = int(len(data) / 4)
                for i in range(0, row):
                    for j in range(0, 4):
                        if j == 0:
                            list4c.append([])
                        list4c[i].append(data[j + i * 4])
                        print(data[j + i * 4])
                        name = QTableWidgetItem(str(data[j + i * 4]))
                        self.tablename.tableWidget.setItem(i, j, name)

    def saveName(self):
        for i in range(0, 4):
            filename = QFileDialog.getSaveFileName(self, 'save file', '/home/jm/study')
            with open(filename[0], 'w') as f:
                my_text = self.textEdit.toPlainText()
                f.write(my_text)
            # for i in range(0,len(list4c)):
            #     for j in range(0,)

