from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QToolButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QDesignerFormEditorInterface
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

class ui_form(object):

    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(376, 155)
        form.move(600,500)
        self.verticalLaoyut = QVBoxLayout(form)
        self.verticalLaoyut.setObjectName("VerticalLayout")
        self.horizontalLayout = QHBoxLayout(form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabelName = QLabel(form)
        self.LabelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.LabelName)
        self.lineEdit = QLineEdit(form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLaoyut.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("HorizontalLayout_2")
        self.labelResult = QLabel(form)
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setFont(QFont("Sanserif", 48))
        self.horizontalLayout_2.addWidget(self.labelResult)
        self.pushButton = QPushButton(form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click_btn)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLaoyut.addLayout(self.horizontalLayout_2)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Muhammad Mohib"))
        self.LabelName.setText(_translate("Form", "Name:"))
        self.pushButton.setText(_translate("Form", "Click"))
        self.pushButton.setGeometry(172, 100, 66, 36)
        self.labelResult.setText(_translate("Form", "TextLabel"))




    def click_btn(self):
        name = self.lineEdit.text()
        print(name)
        self.labelResult.setText(name)



if __name__ == "__main__":
    import sys
    myapp = QApplication(sys.argv)
    faram = QWidget()
    ui = ui_form()
    ui.setupUi(faram)
    faram.show()
    sys.exit(myapp.exec_())

    '''global dall
    dall = self.lineEdit.text()
    #   self.pushButton.setGeometry(100, 100, 66, 36)
    # self.verticalLaoyut.addLayout(self.horizontalLayout_2)'''