from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QDialog, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QApplication
from PyQt5.QtGui import QFont, QIcon
import sys

class mylog(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Practice_1_PyQt5_GUI")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_Table()



    def create_Table(self):

        self.Table = QTableWidget()
        self.Table.setColumnCount(3)
        self.Table.setRowCount(5)
        

        vbox = QVBoxLayout()

        btn1 = QPushButton("Show Data")
        btn1.clicked.connect(self.btn_clicked)

        vbox.addWidget(self.Table)
        vbox.addWidget(btn1)

        self.setLayout(vbox)


    def btn_clicked(self):
        self.Table.setItem(0, 0, QTableWidgetItem("Mohib"))
        self.Table.setItem(0, 1, QTableWidgetItem("20"))
        self.Table.setItem(0, 2, QTableWidgetItem("Yes"))

        self.Table.setItem(1, 0, QTableWidgetItem("Hassaan"))
        self.Table.setItem(1, 1, QTableWidgetItem("16"))
        self.Table.setItem(1, 2, QTableWidgetItem("No"))

        self.Table.setItem(2, 0, QTableWidgetItem("Ahmad"))
        self.Table.setItem(2, 1, QTableWidgetItem("10"))
        self.Table.setItem(2, 2, QTableWidgetItem("No"))

        self.Table.setItem(3, 0, QTableWidgetItem("Maaz"))
        self.Table.setItem(3, 1, QTableWidgetItem("3"))
        self.Table.setItem(3, 2, QTableWidgetItem("No"))

        self.Table.setItem(4, 0, QTableWidgetItem("Wajid"))
        self.Table.setItem(4, 1, QTableWidgetItem("47"))
        self.Table.setItem(4, 2, QTableWidgetItem("Yes"))


app = QApplication(sys.argv)
window = mylog()
window.show()
sys.exit(app.exec_())

