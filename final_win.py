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


    def results(self)  :
        if self.exp.age < 7 :
            self.index = 0 
            return 'Вы слишком малы для этой жести'
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21 :
                return txt_res1
            elif self.index >= 17 and self.index < 21:
                return txt_res2
            elif self.index >= 12 and self.index < 17:
                return txt_res3
            elif self.index >= 6.5 and self.index < 12:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5 :
                return txt_res1
            elif self.index >= 15.5 and self.index < 19.5:
                return txt.txt_res2
            elif self.index >= 10.5 and self.index < 15.5:
                return txt_res3
            elif self.index >= 5 and self.index < 10.5:
                return txt_res4
            else :
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18 :
                return txt_res1
            elif self.index >= 14 and self.index < 18:
                return txt.txt_res2
            elif self.index >= 9 and self.index < 14:
                return txt_res3
            elif self.index >= 3.5 and self.index < 9:
                return txt_res4
            else :
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5 :
                return txt_res1
            elif self.index >= 12.5 and self.index < 16.5:
                return txt.txt_res2
            elif self.index >= 7.5 and self.index < 12.5:
                return txt_res3
            elif self.index >= 2 and self.index < 7.5:
                return txt_res4
            else :
                return txt_res5
        if self.exp.age >= 15 :
            if self.index >= 15 :
                return txt_res1
            elif self.index >= 11 and self.index < 14.9:
                return txt.txt_res2
            elif self.index >= 6 and self.index < 11:
                return txt_res3
            elif self.index >= 0.5 and self.index < 6:
                return txt_res4
            else :
                return txt_res5

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize  (win_width, win_height)
        self.move (win_x, win_y)
    def initUI(self, exp):
        self.results ()
        self.l_line = QVBoxLayout()
        self.text_index = QLabel (txt_index + str(self.index)) #создание виджета 
        self.work_heart = QLabel (txt_workheart + self.results())
        self.l_line.addWidget(self.text_index, alignment= Qt.AlignCenter)
        self.l_line.addWidget(self.work_heart, alignment= Qt.AlignCenter)



        self.setLayout(self.l_line)


