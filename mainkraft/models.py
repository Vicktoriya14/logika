from ursina import *
from settings import *
from ursina.shaders import basic_lighting_shader
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=2, seed=4522)

from random import randint
import pickle
scene.trees = ()


scene.trees = {}


class Tree(Entity):
def __init__(self, pos, **kwargs):
            super().__init__(
                parent=scene,
                model='assets\\minecraft_tree\\scene',
                scale=randint(3,5)
                collider='box',
                position=pos,
                shader=basic_lighting_shader,
                origin_y=0.6,
                **kwargs)
            scene.trees[(self.x, self.y, self.z)] = self

class Block(Button):
        id = 3

        def __init__(self, pos,parent_world, block_id=2, **kwargs):
            super().__init__(
                parent=parent_world,
                model='cube',
                texture=textures[Block.id],
                scale1,
                collider='box',
                position=pos,
                color=color.color(0,0, random.uniform(0.9, 1)),
                highlight_color=color.gray,
                shader=basic_lighting_shader,
                origin_y=-0.5,
                **kwargs)
            parent_world.blocks[(self.x, self.y, self.z)] = self
            self.id = block_id


class Chunk(Entity):
    def __init__(self, chunk_pos,**kwargs):
        super().__init__(model=None, collider=None, shader=basic_lighting_shader, **kwargs)
        self.chunk_pos = chunk_pos
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=3504)
        self.is_simplify = False
        self.default_texture = 2
        self.generate_chunk()
    def simplify_chunk(self):
        if self.is_simplify:
            return

        self.model = self.combine()
        self.collider = 'mesh'
        self.texture = block_textures[self.default_texture]

        for block in self.blocks.values():
            destroy(block)

        self.is_simplify = True

    def detail_chunk(self):
        if not self.is_simplify:
            return

            self.model = None
            self.collider = None
            self.texture = None

            for pos, block in self.block.items():
                new_block = Block(pos, self, block_id = block.id)

            self.is_simplity = False


    def generate_chunk(self):
        cx, cz = self.chunk_pos
        for x in range(CHUNKSIZE):
            for z in range(CHUNKSIZE):
                block_x - cx * CHUNKSIZE + x
                block_z - cz * CHUNKSIZE + z
                y = floor(self.noise([block_x/24, block_z/24])*6)
                block = Block((block_x,y,block_z), self)
                rand-num = randint(0, 200)
                if rand_num == 52:
                    tree = Tree((block_x,y+1,block_z))


        
class WorldEdit(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(**kwargs)
        self.blocks = {}
        self.current_chunk
        self.player = player

    def generate_world(self):
        for x in range(WORLDSIZE):
            for z in range(WORLDSIZE):
                chunk_pos = (x,z)
                if chunk_pos not in self.chunks:
                    chunk = Chunk(chunk_pos)
                    self.chunks[chunk_pos] = chunk

    def save_game(self):
        game_data = (
            "player_pos": (self.player.x, self.player.y, self.player.z),
            "chunks": []
            "trees": []
            "blocks": []


    

        )
        for chunk_pos, chunk in self.chunks.items():
            blocks_data = []
            for block_pos, block in chunk.blocks.items():
                blocks_data.append((block_pos, block.id))

            game_data["chunks"].append((chunk_pos, blocks_data))

        for tree_pos, tree in scene.trees.items():
            game_data['trees'].append((tree_pos, tree.scale))

        with open('save.dat', 'wb') as file:
            pickle.dump(game_data, file)

    def clear_world(self):
        for chunk in self.chunks.values():
            for block in self.blocks.values():
                destroy(block)
            destroy(chunk)
            for tree in scene.trees.values():
                destroy(tree)
                scene.trees.clear()
                self.chunks.clear()


    def load_world(self, chunk_data, tree_data):
        for chunk_pos, blocks in chunk_data:
            chunk = Chunk(chunk_pos)
            for block_pos, block_id in blocks:
                Block(block_pos, chunk, block_id)

            self.chunks[chuk_pos] = chunk

        for tree_pos, tree_scale in tree_data:
            tree = Tree(tree_pos)
            tree.scale = tree_scale






    def load_game(self):
        
        with open('save.dat', 'rb') as file:
            game_data = pickle.load(file)

            self.clear_world()
            self.player.x, self.player.y, self.player.z = game_data["player_pos"]
            self.load_world(game_data["chunks"], game_data["trees"])
            print("Гру завантажено")



    def input(self, key):
        if key == 'k':
            self.save_game()
        if key == '1':
            self.load_game()


        


        

    def input(self, key):
            if key == 'left mouse down':
                hit_info = raycast(camera.world_position, camera.forward, distance=10)
                if hit_info.hit:
                    block = Block(hit_info.entity.position + hit_info.normal, hit_info.entity.parent, Block.id)
            if key == 'right mouse down' and mouse.hovered_entity:
                if isinstance(mouse.hovered_entity, Block):
                    block = mouse.hovered_entity
                    chunk = block.parent
                    del chunk.blocks[(block.x, block.y, block.z)]
                    destroy(mouse.hovered_entity)
                if isinstance(mouse.hovered_entity, Tree):
                    tree = mouse.hovered_entity
                    del scene.trees[(tree.x, tree.y, tree.z)]
                    destroy(tree)


            

            if key == 'sroll up':
                Block.id+=1
                if len(textures)<=Block.id
                      Block.id = 0

            
            if key == 'sroll down':
                Block.id+=1
                if Block.id<0:
                     Block.id = len(textures)-1
                     

    def update(self):
        player_pos = self.player.possition
        for chunk_pos, chunk in self.chunk.items():
            chunk_world_pos = Vec3(chunk_pos[0] * CHUNKSIZE, 0, chunk_pos[1]*CHUNKSIZE)
            d = distance(player_pos, chunk_world_pos)
            if d < DETAIL_DISTANCE and chunk.is_simplify:
                chunk.detail_chunk()
            elif d >= DENAIL_DISTANCE and not chunk.is_simplify:
                chunk.simply_chunk()
                



      
            
        

