from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os

app = QApplication([])
window = QWidget()


btn_folder = QPushButton('Папка')
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
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

def showFiles():
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)

    graphic_files = filter(files)

    lst_files.clear()
    lst_files.addItems(graphic_files)

class ImageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = 'Modified/'


def load_image(self,filename):
    self.filename = filename
    full_path = os.path.join(workdir, filename)
    self.original = Image.open(full_path)

def show_image(self, path):
    lb_pic.hide()
    w, h = lb_pic.width(), lb_pic.height()

    pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)

    lb_pic.setPixmap(pixmapimage)
    lb_pic.show()

def saveAndShowImage(self):
    path = os.path.join(workdir, self.save_dir)
    if not (os.path.exists(path) or os.path.isdir(path)):
        os.mkdir(path)

    image_path = os.path.join(path, self.filename)
    self.original.save(image_path)
    self.show_image(image_path)


def showChosenItems():
    filename = lst_files.currentItem().text()
    workdimage.load_image(filename)
    full_path = os.path.join(workdir, filename)
    workdimage.show_image(full_path)

workdimage = ImageProcessor()


lst_files.currentRowChanged.connect(showChosenItems)
btn_folder.clicked.connect(showFiles)


window.setLayout(layout_editor)
window.show()
app.exec_()