from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os

app = QApplication([])
window = QWidget()


btn_folder = QPushButton('Папка')
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Впріво')
btn_flip = QPushButton('Дзеркало')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('Ч/Б')

lst_files = QListWidget()
lb_pic = QLabel('Картинки')

layout_editor = QHBoxLayout()

col1 = QVBoxLayout()
col2 =QVBoxLayout()

row = QHBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(lst_files)

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
row.addWidget(btn_bw)

col2.addWidget(lb_pic)
col2.addLayout(row)

layout_editor.addLayout(col1, 1)
layout_editor.addLayout(col2, 4)

workdir = QFileDialog.getExistingDirectory()
files = os.listdir(workdir)

def filter(filenames):
    result = []
    ext = ['jpg', 'png', 'jpeg', 'bmp', 'gif']

    for file in filenames:
        if file.split('.')[-1] in ext:
            result.append(file)

    return result


window.setLayout(layout_editor)
window.show()
app.exec_()