from PyQt5.QtWidgets import QApplication, QDialog,QVBoxLayout, QHBoxLayout, QLCDNumber, QPushButton
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from random import randint




class Window(QDialog):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("QLCDNubmer_PyQt5")
        self.setWindowIcon(QIcon("burger.ico"))


        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet("background-color:yellow")

        vbox.addWidget(self.lcd)


        button = QPushButton("Create Random Number")
        button.setStyleSheet("background-color:blue")
        button.setFont(QFont("Sanserif", 22))
        button.clicked.connect(self.rand_generators)


        vbox.addWidget(button)

        self.setLayout(vbox)

    def rand_generators(self):
        randoms = randint(1, 300)
        self.lcd.display(randoms)









app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
