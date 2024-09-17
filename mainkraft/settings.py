



import os
from ursina import *






MAPSIZE = 10

BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'assets/texture')
texture = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
     texture = load_texture('assets/texture' + os.sep + image)
     texture.append(texture)
