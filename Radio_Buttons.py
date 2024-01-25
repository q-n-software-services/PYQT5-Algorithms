from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QRadioButton, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont, QImage
from PyQt5.QtCore import QSize
class window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 Radio Button")
        self.setWindowIcon(QIcon('masjid.ico'))

        self.setStyleSheet("background-color:Orange")

        self.create_RadioButtons()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.label = QLabel("")
        self.label.setFont(QFont("Sanserif", 22))
        vbox.addWidget(self.label)



        self.setLayout(vbox)



    def create_RadioButtons(self):
        self.groupbox = QGroupBox("What is your Favourite Sport ?")
        self.groupbox.setFont(QFont("Sanserif", 22))
        

        hbox = QVBoxLayout()
        self.rad1 = QRadioButton("Football")

        self.rad1.setIcon(QIcon("burger.ico"))
        self.rad1.setIconSize(QSize(80, 80))
        self.rad1.setFont(QFont("Sanserif", 27))
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Cricket")

        self.rad2.setIcon(QIcon("masjid.ico"))
        self.rad2.setIconSize(QSize(80, 80))
        self.rad2.setFont(QFont("Sanserif", 27))
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("Badminton")

        self.rad3.setIcon(QIcon("burger.ico"))
        self.rad3.setIconSize(QSize(80, 80))
        self.rad3.setFont(QFont("Sanserif", 27))
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)


        self.groupbox.setLayout(hbox)


    def on_selected(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            self.label.setText("You have selected:\t" + radio_button.text())






app = QApplication(sys.argv)
Window = window()
Window.show()
sys.exit(app.exec_())