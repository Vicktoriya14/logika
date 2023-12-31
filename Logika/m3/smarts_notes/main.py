from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

def writeToFile():
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)

app = QApplication([])
window = QWidget()

field_text = QTextEdit()
lb_notes = QLabel('Список заміток')
lst_notes = QListWidget()

btn_note_creat = QPushButton('Створити замітку')
btn_note_delet = QPushButton('Видалити замітку')
btn_note_save = QPushButton('Зберегти замітку')


lb_tegs = QLabel('Список тегів')
lst_tegs = QListWidget()
field_tag = QLineEdit()


btn_tegs_add = QPushButton('Додати до замітки')
btn_tegs_unpin = QPushButton('Відкрити від замітки')
btn_tegs_search = QPushButton('Шукати замітки за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)


col1.addWidget(field_text)

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_creat)
row1.addWidget(btn_note_delet)
row1.addWidget(btn_note_save)

col2.addLayout(row1)

window.setLayout(layout_notes)


col2.addWidget(lb_tegs)
col2.addWidget(lst_tegs)


field_tag = QLineEdit()
col2.addWidget(field_tag)

row2 = QHBoxLayout()
row2.addWidget(btn_tegs_add)
row2.addWidget(btn_tegs_unpin)
row2.addWidget(btn_tegs_search)


col2.addLayout(row2)

window.setLayout(layout_notes)




with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)

def show_note():
    key = lst_notes.currentItem().text()
    field_text.setText(notes[key]['текст'])

    lst_tegs.clear()
    lst_tegs.addItems(notes[key]['теги'])


def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', 'Назва замітки')

    if note_name and ok:
        notes[note_name] = {"текст": "", "теги": []}
        lst_notes.addItem(note_name)

def save_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        notes[key]['текст'] = field_text.toPlainText()

        writeToFile()

def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del notes[key]

        field_text.clear()
        lst_tegs.clear()
        lst_notes.clear()

        lst_notes.addItems(notes)
        writeToFile()

def add_tag():
    key = lst_notes.currentItem().text()
    tag = field_tag.text()

    notes[key]['теги'].append(tag)

    lst_tegs.addItem(tag)
    field_tag.clear()

    writeToFile()


def del_tag():
    key = lst_notes.currentItem().text()
    tag = lst_tegs.currentItem().text()

    notes[key]['теги'].remove(tag)

    lst_tegs.clear()
    lst_tegs.addItems(notes[key]['теги'])

    writeToFile()

def search_tag():
    tag = field_tag.text()

    if btn_tegs_search.text() == 'Шукати замітки за тегом':
        filtered_notes = {}

        for key in notes:
            if tag in notes[key]['теги']:
                filtered_notes[key] = notes[key]

        btn_tegs_search.setText('скинути пошук')


        lst_notes.clear()
        lst_notes.addItems(filtered_notes)

        field_text.clear()
        lst_tegs.clear()
    elif btn_tegs_search.text() == 'скинути пошук':
        btn_tegs_search.setText('Шукати замітки за тегом')


        field_text.clear()
        lst_notes.clear()
        lst_tegs.clear()
        field_tag.clear()

        lst_notes.addItems(notes)

lst_notes.itemClicked.connect(show_note)
btn_note_delet.clicked.connect(del_note)
btn_note_creat.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)

btn_tegs_add.clicked.connect(add_tag)
btn_tegs_unpin.clicked.connect(del_tag)
btn_tegs_search.clicked.connect(search_tag)

lst_notes.addItems(notes)

window.setLayout(layout_notes)
window.show()
app.exec_()