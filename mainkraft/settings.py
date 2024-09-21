



import os
from ursina import *


CHUNKSIZE = 10
WORLDSIZE = 3


MAPSIZE = 10

BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'assets/texture')
textures = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
     texture = load_texture('assets/texture' + os.sep + image)
     textures.append(texture)
