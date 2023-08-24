from memo___card_layout import *
from PyQt5.QtWidgets  import QWidget, QApplication
from random import shuffle # будемо змішувати відповіді в картці питання
from memo___data import *

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

frm = Question('Яблуко', 'Apple', 'Caterpiller', 'house', 'cat')
frm_card = QuestionView(frm, lb_Question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])

def show_data():
    
    pass

def check_result():
    
    pass

win_card = QWidget()
win_card.resize(card_width, card_height)

frm_card.show()
win_card.setLayout(layout_card)
win_card.show()
app.exec_()