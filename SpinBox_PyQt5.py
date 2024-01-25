from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QLineEdit
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QDialog):
    def __init__(self):
        super().__init__()


        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("SpinBox_PyQt5")
        self.setWindowIcon(QIcon('burger.ico'))

        self.create_spinbox()


    def create_spinbox(self):
        hbox = QHBoxLayout()

        label = QLabel("Laptop Price: \t")

        self.lineEdit = QLineEdit()
        self.spinbox = QSpinBox()

        self.spinbox.valueChanged.connect(self.spin_selected)
        self.total_Result = QLineEdit()



        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_Result)



        self.setLayout(hbox)


    def spin_selected(self):
        if self.lineEdit != 0:
            price = int(self.lineEdit.text())
            TotalPrice = self.spinbox.value() * price


            self.total_Result.setText(str(TotalPrice))

        else:
            print("Wrong Value")















app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
