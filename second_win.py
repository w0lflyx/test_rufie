# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit,)
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from final_win import *
from instr import *

class Experiment():
    def __init__ (self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
        


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
        self.button1 = QPushButton(txt_starttest1 , self)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.text_test2 = QLabel(txt_test2)
        self.button2 = QPushButton(txt_starttest2, self)
        self.text_test3 = QLabel(txt_test3)
        self.button3 = QPushButton(txt_starttest3, self)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)
        self.button4 = QPushButton(txt_sendresults, self)
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
    

    def next_click(self):
        
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.tw = FinalWin(self.exp)

    def timer_test(self): #функция вызывается по нажатию кнопки баттон 1
        global time
        time = QTime (0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000) #каждую секунду
        
    
    def timer1Event(self): #функция вызывается каждую секунду
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color, rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == ('00:00:00'):
            self.timer.stop()
    
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500) #одно приседание = полторы сек 
    
    def timer2Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color, rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == ('00:00:00'):
            self.timer.stop()
    
    def timer_last(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)


    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss"[6:8]) )>= 45:
            self.text_timer.setStyleSheet("color:rgb(0, 255, 0)")
        elif  int(time.toString("hh:mm:ss"[6:8]))<= 15: 
            self.text_timer.setStyleSheet("color:rgb(0, 255, 0)")
        else:
            self.text_timer.setStyleSheet("color, rgb(0, 0, 0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == ('00:00:00'):
            self.timer.stop()
        
    def connects(self):
        self.button4.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_sits)
        self.button3.clicked.connect(self.timer_last)