from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QDialog):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("CheckBox_PyQt5")
        self.setWindowIcon(QIcon('burger.ico'))
        self.create_Checkbox()


    def create_Checkbox(self):
        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Football")
        self.check1.setIcon(QIcon('burger.ico'))
        self.check1.setIconSize(QSize(50, 50))
        self.check1.setFont(QFont("Sanserif", 22))
        self.check1.toggled.connect(self.item_selected)
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox("Cricket")
        self.check2.setIcon(QIcon('masjid.ico'))
        self.check2.setIconSize(QSize(50, 50))
        self.check2.setFont(QFont("Sanserif", 22))
        self.check2.toggled.connect(self.item_selected)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("Burger")
        self.check3.setIcon(QIcon('burger.ico'))
        self.check3.setIconSize(QSize(50, 50))
        self.check3.setFont(QFont("Sanserif", 22))
        self.check3.toggled.connect(self.item_selected)

        hbox.addWidget(self.check3)

        vbox = QVBoxLayout()
        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 27))
        self.label.setStyleSheet("color:red")
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def item_selected(self):
        value = ""

        if self.check1.isChecked():
            value = value + "\t" +  self.check1.text()

        if self.check2.isChecked():
            value = value + "\t" + self.check2.text()

        if self.check3.isChecked():
            value = value + "\t" +  self.check3.text()

        if value == "":
            value = "Nothing Selected"
        else:
            value = "You have selected:\t" + value

        self.label.setText(value)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
