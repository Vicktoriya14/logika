from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController

from perlin_noise import PerlinNoise
from numpy import floor

app = Ursina()
MAPSIZE = 10

class Block(Button):
        def __init__(self, pos, **kwargs):
                super().__init__(
                    parent=scene,
                    model='cube',
                    texture='wood.png',
                    scale=1,
                    collider='box',
                    position=pos,
                    color=color.color(0,0. random.uniform(0.9, 1)),
                    origin_y=-0.5,
                    **kwargs)

                



player = FirstPersonController()

sky = Sky(texture='sky_sunset')



#ground = Entity(model='quad', texture="grass", scale=64, textute_scale=(16,16) ,rotation=90,
#               colider='box', position=(-2, 0,0))

noise = PerlinNoise(octaves=2, seed=4522)

for x in range(-MAPSIZE, MAPSIZE):
        for z in range(-MAPSIZE, MAPSIZE):
            y = floor(noise([x/24, z/24])*6)
            block = Block((x,0,z))

window.fullscreen = True
app.run()
