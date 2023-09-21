from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

app = QApplication([])

window = QWidget()

field_text = QTextEdit()
lb_notes = QLabel('Список заміток')
lst_notes = QListWidget()

btn_note_creat = QPushButton('Створити замітку')
btn_note_delet = QPushButton('Видалити замітку')
btn_note_save = QPushButton('Зберегти замітку')


field_text = QTextEdit()
lb_notes_tegs = QLabel('Список тегів')
lst_notes_tegs = QListWidget()

btn_note_add = QPushButton('Додати до замітки')
btn_note_unpin = QPushButton('Відкрити від замітки')
btn_note_search = QPushButton('Шукати замітки за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)

col1.addWidget(field_text)


col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_creat)
row1.addWidget(btn_note_delet)
row1.addWidget(btn_note_save)

col2.addLayout(row1)

window.setLayout(layout_notes)


col2.addWidget(lb_notes_tegs)
col2.addWidget(lst_notes_tegs)

row2 = QHBoxLayout()
row2.addWidget(btn_note_add)
row2.addWidget(btn_note_unpin)
row2.addWidget(btn_note_search)

col2.addLayout(row2)

window.setLayout(layout_notes)


with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)

window.setLayout(layout_notes)
window.show()
app.exec_()