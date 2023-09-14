# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
class TestWin(QWidget):
    def __init__ (self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize  (win_width, win_height)
        self.move (win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line =  QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.text_name = QLabel (txt_name) #создание виджета 
        self.line_name = QLineEdit(txt_hintname)
        self.text_age = QLabel (txt_age) #создание виджета 
        self.line_age = QLineEdit(txt_hintage)
        self.text_test1 =  QLabel(txt_test1) 
        self.button1 = QPushButton(txt_hinttest1 , self)
        self.line_test1 = QLineEdit(txt_starttest2)
        self.text_test2 = QLabel(txt_test2)
        self.button2 = QPushButton(txt_starttest2, self)
        self.text_test3 = QLabel(txt_test3)
        self.button3 = QPushButton(txt_starttest3, self)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test2 = QLineEdit(txt_hinttest3)
        self.button4 = QLineEdit(txt_sendresults, self)
        self.text_timer = QLabel(txt_timer)
        self.l_line.addWidget(self.text_name, alignment= Qt.AlignLeft) #добавление его на направляющую
        self.l_line.addWidget(self.line_name, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment= Qt.AlignLeft) 
        self.l_line.addWidget(self.line_age, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment= Qt.AlignLeft )
        self.l_line.addWidget(self.button2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.button4, alignment= Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer, alignment= Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        
        self.setLayout(self.h_line)
    def connects(self):
        pass
