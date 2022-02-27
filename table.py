from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        hhbox = QHBoxLayout()  # 横向布局

        tableWidget = QTableWidget()  # 创建一个表格

        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(4)  # 5行4列

        tableWidget.setHorizontalHeaderLabels(['第一行列', '第二列', '第三列', '第四列'])
        tableWidget.setVerticalHeaderLabels(['第一行', '第二行', '第三行', '第四行', '第五行'])
        # 表头

        hhbox.addWidget(tableWidget)  # 把表格加入布局

        self.setLayout(hhbox)  # 创建布局

        self.setWindowTitle("人员名单")
        self.resize(600, 250)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Example()
    sys.exit(app.exec_())