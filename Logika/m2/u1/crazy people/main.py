from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_window = QWidget()

button = QPushButton('Згенерувати')
text = QLabel('Натисни щоб дізнатися переможця')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text)
line.addWidget(winner)
line.addWidget(button)

def win():
    ran = randint(1, 1000)
    winner.setText(str(ran))

button.clicked.connect(win)


main_window.setLayout(line)

main_window.show()
app.exec_()
