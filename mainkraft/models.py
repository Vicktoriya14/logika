from ursina import *
from settings import *
from ursina.shaders import basic_lighting_shader
from perlin_noise import PerlinNoise
noise = PerlinNoise(octaves=2, seed=4522)
class Block(Button):
        id = 1


        def __init__(self, pos, **kwargs):
            super().__init__(
                parent=generade_world,
                model='cube',
                texture=textures[Block.id],
                scale=1,
                collider='box',
                position=pos,
                color=color.color(0,0, random.uniform(0.9, 1)),
                highlight_color=color.gray,
                shader=basic_lighting_shader,
                origin_y=-0.5,
                **kwargs)

                
        
class WorldEdit(Entity):
    def _init_(self,**kwargs):
        super().__init__(**kwargs)
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=4522)

    def generate_world(self):
        for x in range(-MAPSIZE, MAPSIZE):
            for z in range(-MAPSIZE, MAPSIZE):
                y = floor(noise([x/24, z/24])*6)
                block = Block((x,y,z), self)
                self.blocks[(x,y,z)] = block

    def input(self, key):
            if



            

            if key == 'sroll up':
                Block.id+=1
                if Block.id<0:
                     Block.id = len(texture)-1

            
            if key == 'sroll down':
                Block.id+=1
                if Block.id<0:
                     Block.id = len(texture)-1

      
            
        

