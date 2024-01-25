from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QToolButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
import sys
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui




mydata12 = None

class window_example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("MUHAMMADMohib.pk")
        self.setWindowIcon(QIcon('masjid.ico'))
        self.setStyleSheet('background-color:green')
        self.create_buttons()
        self.show()
    def create_buttons(self):
        btn1 = QPushButton("Click Me", self)
        btn1.setGeometry(92, 100, 112, 57)
        btn1.setIcon(QIcon('masjid.ico'))
        btn1.setStyleSheet('color:white')
        btn1.setStyleSheet('background-color:blue')
        btn1.setIconSize(QtCore.QSize(112, 57))
        btn1.clicked.connect(self.btn1_clicked)



        btn2 = QPushButton("Second Button", self)
        btn2.setGeometry(208, 100, 112, 57)
        btn2.setStyleSheet("background-color:red")
        btn2.setIcon(QIcon('burger.ico'))
        btn2.clicked.connect(self.btn2_clicked)
        btn2.setIconSize(QtCore.QSize(112, 57))

        btn3 = QPushButton(" 3", self)
        btn3.setGeometry(92, 165, 235, 235)
        btn3.setStyleSheet("background-color:yellow")
        btn3.setIcon(QIcon("burger.ico"))
        btn3.setIconSize(QtCore.QSize(235, 235))
        btn3.clicked.connect(self.btn3_clicked)

        btn4 = QPushButton(" x ", self)
        btn4.setGeometry(262, 165, 66, 34)
        btn4.setStyleSheet("background-color:white")
        btn4.clicked.connect(self.Xbtn3_clicked)






        lyout = QGridLayout()
        lyout.addWidget(btn1, 0, 0)
        lyout.addWidget(btn2, 0, 1)
        lyout.addWidget(btn3, 1, 0)
        lyout.addWidget(btn4, 1, 1)

        self.setLayout(lyout)



    def btn1_clicked(self):
        print("Button One Clicked")

    def btn2_clicked(self):
        print("Button TWO Clicked")

    def btn3_clicked(self, num):
        if not num:
            num = 1

        print("Button Three Clicked", num, "times")

    def Xbtn3_clicked(self):
        a = input("Enter Quantity")
        self.btn3_clicked(a)










        









app = QApplication(sys.argv)
window = window_example()
window.show()
sys.exit(app.exec_())


