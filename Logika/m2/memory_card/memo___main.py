from memo___card_layout import *
from PyQt5.QtWidgets  import QWidget, QApplication
from random import shuffle # будемо змішувати відповіді в картці питання

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

def show_data():
    
    pass

def check_result():
    
    pass

win_card = QWidget()
win_card.resize(card_width, card_height)


win_card.setLayout(layout_card)
win_card.show()
app.exec_()