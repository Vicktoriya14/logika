from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController

from numpy import floor
from perlin_noise import PerlinNoise

from ursina.shaders import basic_lighting_shader


app = Ursina()
from settings import *

from models import Block, WorldEdit


player = FirstPersonController()

sky = Sky(texture='sky_sunset')

light = DirectionalLight(shadows=True,)
light.look_at(Vec3(1,-1,1))

world = WorldEdit(player)
world.generate_world()


#scene.fog_density = (5, 50)   # sets linear density start and end





window.fullscreen = True
app.run()
