from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *

class FinalWin(QWidget):
    def __init__ (self, exp):
        super().__init__()
        self.set_appear()
        self.initUI()

        self.show()


    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize  (win_width, win_height)
        self.move (win_x, win_y)
    def initUI(self):
        self.l_line = QVBoxLayout()
        self.text_index = QLabel (txt_index) #создание виджета 
        self.work_heart = QLabel (txt_workheart)
        self.l_line.addWidget(self.text_index, alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.work_heart, alignment= Qt.AlignCenter)



        self.setLayout(self.l_line)


        