import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,QMainWindow,
                             QSplitter,QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topleft.setGeometry(QtCore.QRect(0, 0, 20, 100))

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        right= QFrame(self)
        right.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter1.setGeometry(QtCore.QRect(0, 0,400, 100))

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setGeometry(QtCore.QRect(0, 400, 400, 100))

        splitter3 = QSplitter(Qt.Horizontal)
        splitter3.addWidget(splitter2)
        splitter3.addWidget(right)

        hbox.addWidget(splitter3)
        self.setLayout(hbox)

        self.setGeometry(500, 500, 500, 300)
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self, text):
        self.rbl.setText(text)
        self.rbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())