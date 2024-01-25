from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLCDNumber, QLabel, QWidget, QPushButton, QFileDialog,QLineEdit, QTextEdit
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer, Qt
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.setGeometry(0, 0, 1350, 700)
        self.setWindowTitle("Website Builder")
        self.setWindowIcon(QIcon("burger.ico"))
        self.setStyleSheet("background-color:White")

        self.main_function()

    def main_function(self):
        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        label = QLabel("Website Builder")
        label.setStyleSheet("background-color:cyan; color: white;")
        label.setFont(QFont("times new roman", 48))
        label.setFixedHeight(72)
        # label.setFixedWidth(600)
        label.setAlignment(Qt.AlignCenter)
        vbox1.addWidget(label)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setStyleSheet("background-color:white;")
        self.line_edit1.setFont(QFont("times new roman", 27))
        self.line_edit1.setFixedHeight(48)
        # label.setFixedWidth(600)
        self.line_edit1.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(self.line_edit1)


        btn1 = QPushButton("Browse")
        btn1.setStyleSheet("background-color:magenta; color: white;")
        btn1.setFont(QFont("times new roman", 22))
        btn1.setFixedHeight(44)
        btn1.setFixedWidth(100)
        btn1.clicked.connect(self.open)
        hbox1.addWidget(btn1)

        vbox1.addLayout(hbox1)

        self.line_edit1 = QLineEdit()
        self.line_edit1.setStyleSheet("background-color:white;")
        self.line_edit1.setFont(QFont("times new roman", 27))
        self.line_edit1.setFixedHeight(48)
        # label.setFixedWidth(600)
        self.line_edit1.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(self.line_edit1)

        btn1 = QPushButton("Browse")
        btn1.setStyleSheet("background-color:magenta; color: white;")
        btn1.setFont(QFont("times new roman", 22))
        btn1.setFixedHeight(44)
        btn1.setFixedWidth(100)
        btn1.clicked.connect(self.open)
        hbox1.addWidget(btn1)

        vbox1.addLayout(hbox1)


        source_articles_folder = "path from file explorer"
        templates_folder = 'template source path from file explorer'
        youtube_keywords = 'jnk'
        site_name = 'Q N Software Services'
        type_of_site = "drop down list: 1. Simple Video Site 2, 3 etc"
        source_of_videos = "dropdown list: 1 The Current Youtube Feed, 2, 3 etc"
        youtube_feed_to_use = 'drop down list'
        number_of_video_pages = 600

        primary_ad = 'new dialog box'
        amazon_search_buttons = 'text box'
        amazon_affiliate_id = 'lkmdf653421fsx'
        search_domain = 'shoes'
        adsense_id = 'jbhkdfn paste button option as for file explorer'
        ad_unit_code = 'text box paste button option as for file explorer'
        google_analytics_id = 'ghvjsdf654312sdf'
        remote_assets_folder = 'path or a string'
        output_folder = 'path from file explorer'

        btn_create = QPushButton("Create")
        btn_create.setStyleSheet("background-color:blue; color: white;")
        btn_create.setFont(QFont("times new roman", 22))
        btn_create.setFixedHeight(44)
        btn_create.clicked.connect(self.create_submit)
        vbox1.addWidget(btn_create)


        self.setLayout(vbox1)

    def open(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        print(path[0])
        self.line_edit1.setPlaceholderText(path[0])
        return path[0]

    def create_submit(self):
        pass











app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
