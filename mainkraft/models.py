from ursina import *
from settings import *
from ursina.shaders import basic_lighting_shader
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=2, seed=4522)

from random import randint

class Tree(Entity):
def __init__(self, pos,parent_world, **kwargs):
            super().__init__(
                parent=parent_world,
                model='assets\\minecraft_tree\\scene',
                scale=randint(3,5)
                texture=textures[Block.id],
                scale=,
                collider='box',
                position=pos,
                
                shader=basic_lighting_shader,
                origin_y=0.5,
                **kwargs)
class Block(Button):
        id = 1

        def __init__(self, pos,parent_world, **kwargs):
            super().__init__(
                parent=parent_world,
                model='cube',
                texture=textures[Block.id],
                scale=3,
                collider='box',
                position=pos,
                color=color.color(0,0, random.uniform(0.9, 1)),
                highlight_color=color.gray,
                shader=basic_lighting_shader,
                origin_y=-0.5,
                **kwargs)

class Chunk(Entity):
    def __init__(self, chunk_pos,**kwargs):
        super().__init__(model=None, collider=None, shader=basic_lighting_shader, **kwargs)
        self.chunk_pos = chunk_pos
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=4522)
        self.generate.chunk()

    def generate_chunk(self):
        cx, cz = self.chunk_pos
        for x in range(-CHUNKSIZE, CHUNKSIZE):
            for z in range(-CHUNKSIZE, CHUNKSIZE):
                block_x - cx * CHUNKSIZE + x
                block_z - cz * CHUNKSIZE + z
                y = floor(noise([x/24, z/24])*6)
                block = Block((block_x,y,block_z), self)
                self.blocks[(block_x,y,block_z)] = block

                rand-num = randint(0, 200)
                if rand_num == 52:
                    tree = Tree((x,y+1,z), self)


        
class WorldEdit(Entity):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.blocks = {}
        self.current_chunk

    def generate_world(self):
        for x in range(WORLDSIZE):
            for z in range(WORLDSIZE):
                chunk_pos = (x,z)
                if chunk_pos not in self.chunks:
                    chunk = Chunk(chunk_pos)
                    chunk.generate_chunk()
                   

        

    def input(self, key):
            if key == 'left mouse down':
                hit_info = raycast(camera.world_position, camera.forward, distance=10)
                if hit_info.hit:
                    block = Block(hit_info.entity.position + hit_info.normal, self)
            if key == 'right mouse down' and mouse.hovered_entity:
                destroy(mouse.hovered_entity)


            

            if key == 'sroll up':
                Block.id+=1
                if Block.id<0:
                     Block.id = len(textures)-1

            
            if key == 'sroll down':
                Block.id+=1
                if Block.id<0:
                     Block.id = len(textures)-1

      
            
        

