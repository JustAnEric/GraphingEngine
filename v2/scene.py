from model import *
from random import randint
from time import sleep, time

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

MAPSIZE = 50

portionInto = 2
howManyInPortion = int(MAPSIZE/portionInto)
lastPos = None

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.CHUNKS = []
        self.BLOCKS = []
        self.FLOOR_BLOCKS = []
        self.mobs = []
        self.load()
    
    def add_object(self, obj):
        self.objects.append(obj)
        return obj

    def wait_until(self, somepredicate, timeout, period=0.25, *args, **kwargs):
        mustend = time() + timeout
        while time() < mustend:
            if somepredicate(*args, **kwargs): return True
            sleep(period)
        return False


    def no_halt_sleep(self, seconds:int):
        done = False
        def sleepf():
            sleep(seconds)
            done = True
        self.wait_until(lambda: done == True, 10000000)
        return done

    def load(self):
        app = self.app
        add = self.add_object

        #add(Cube(app))
        n,s = MAPSIZE,inc_sbm
        #self.mobs.append({
            #"position": {
                #"x": 0,
                #"y": 1,
                #"z": 0
            #},
            #"shape": "cube",
            #"texture": [4],
            #"type": "block",
            #"block": add(BumMilkshake(app, (0,1,0), (0,0,0)))
        #})
        for x in range(-n, n,s):
            global lastPos
            for z in range(-n,n,s):
                cubepos = (x, -s, z)
                obj = Cube(app, pos=cubepos)
                identifier_number = randint(0,111111111111111111111111111111111111111111)
                add(obj)
                self.BLOCKS.append({
                    "position": {
                        "x": x,
                        "y": -s,
                        "z": z
                    },
                    "shape": "cube",
                    "texture": [0],
                    "type": "block",
                    "id": identifier_number
                })
                self.FLOOR_BLOCKS.append({
                    "position": {
                        "x": x,
                        "y": -s,
                        "z": z
                    },
                    "shape": "cube",
                    "texture": [0],
                    "type": "block",
                    #"isRemoved": False,
                    #"isVisible": True,
                    "id": identifier_number
                })
                lastPos = cubepos

        maxTrees = 115
        for x in range(randint(0,maxTrees),maxTrees):
                self.build_tree(pos=(randint(-MAPSIZE,MAPSIZE), s-2, randint(-MAPSIZE,MAPSIZE)))
                #-(4*2.5)

    def build_tree(self,pos=(0,0,0)):
        add = self.add_object
        app = self.app
        add(Cube(app, pos=pos, tex_id=1))
        add(Cube(app, pos=(pos[0], pos[1]+(inc_sbm*1), pos[2]), tex_id=1))
        add(Cube(app, pos=(pos[0], pos[1]+(inc_sbm*2), pos[2]), tex_id=1))
        #sides
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*2), pos[2]), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*2), pos[2]), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*2), pos[1]+(inc_sbm*2), pos[2]), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-2), pos[1]+(inc_sbm*2), pos[2]), tex_id=2))

        add(Cube(app, pos=(pos[0], pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-1)), tex_id=2))
        add(Cube(app, pos=(pos[0], pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0], pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-2)), tex_id=2))
        add(Cube(app, pos=(pos[0], pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*2)), tex_id=2))

        # create diagonal
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-1)), tex_id=2))

        # create subdiagonal 1
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*2)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-2)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*2)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-2)), tex_id=2))

        # create subdiagonal 2
        add(Cube(app, pos=(pos[0]+(inc_sbm*-2), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*2), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*2), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-2), pos[1]+(inc_sbm*2), pos[2]+(inc_sbm*-1)), tex_id=2))

        # 2nd layer

        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*-1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*1)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*-1)), tex_id=2))

        add(Cube(app, pos=(pos[0]+(inc_sbm*1), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*-1+2)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*1-2)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*1-2), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*1+0)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1+2), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*-1+0)), tex_id=2))
        add(Cube(app, pos=(pos[0]+(inc_sbm*-1+2), pos[1]+(inc_sbm*3), pos[2]+(inc_sbm*-1+2)), tex_id=2)) # middle part of leaves (2nd layer)

        # 3rd layer

        add(Cube(app, pos=(pos[0]+(inc_sbm*-1+2), pos[1]+(inc_sbm*4), pos[2]+(inc_sbm*-1+2)), tex_id=2)) # middle part of leaves (3rd layer)

    def build_cobblestone_layer(self):
        add = self.add_object
        n,s = MAPSIZE,inc_sbm
        app = self.app
        for x in range(-n, n,s):
            global lastPos
            for z in range(-n,n,s):
                cubepos = (x, -s-2, z)
                obj = Cube(app, pos=cubepos)
                identifier_number = randint(0,111111111111111111111111111111111111111111)
                add(obj)
                self.BLOCKS.append({
                    "position": {
                        "x": x,
                        "y": -s-2,
                        "z": z
                    },
                    "shape": "cube",
                    "texture": [0],
                    "type": "block",
                    "id": identifier_number
                })
                lastPos = cubepos

    def clear_map_floor(self):
        collectedObjects = []
        for i in self.FLOOR_BLOCKS:
            for index,z in enumerate(self.objects):
                if i['id'] == z.identifier:
                    collectedObjects.append(index)
        self.FLOOR_BLOCKS.clear()
        for i in collectedObjects:
            del self.objects[i]
            print("* Removed floor blocks")

    def make_chunks_array(self):
        chunks = self.CHUNKS
        for x in range(-howManyInPortion,howManyInPortion):
            chunkarr = {
                "chunkId": x,
                "chunkStartCoordinates": (MAPSIZE/portionInto+2,1,MAPSIZE/portionInto+2),
                "chunkEndCoordinates": (MAPSIZE/portionInto,1,1)
            }
    
    def render_new_chunk(self, chunk_number, pos):
        add = self.add_object
        app = self.app
        self.clear_map_floor()
        n,s = MAPSIZE,inc_sbm
        for x in range(-n, n,s):
            for z in range(-n,n,s):
                add(Cube(app, pos=(x, -s, z)))

    def render(self):
        for obj in self.objects:
            obj.render()