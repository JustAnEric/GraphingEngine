from model import *
from random import randint
from time import sleep, time

MAPSIZE = 126

portionInto = 3
howManyInPortion = int(MAPSIZE/portionInto)
lastPos = None

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.CHUNKS = []
        self.BLOCKS = []
        self.load()
    
    def add_object(self, obj):
        self.objects.append(obj)

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
        n,s = howManyInPortion,inc_sbm
        for x in range(-n, n,s):
            global lastPos
            for z in range(-n,n,s):
                cubepos = (x, -s, z)
                obj = Cube(app, pos=cubepos)
                add(obj)
                self.BLOCKS.append({
                    "position": {
                        "x": x,
                        "y": -s,
                        "z": z
                    },
                    "shape": "cube",
                    "texture": [0],
                    "type": "block"
                })
                lastPos = cubepos

        maxTrees = 115
        for x in range(randint(0,maxTrees),maxTrees):
                self.build_tree(pos=(randint(-MAPSIZE,MAPSIZE), s-2.5, randint(-MAPSIZE,MAPSIZE)))
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
    
    def render_new_chunk(self, chunk_number, pos):
        add = self.add_object
        app = self.app
        n,s = MAPSIZE,inc_sbm
        for x in range(-n, n,s):
            for z in range(-n,n,s):
                add(Cube(app, pos=(x, -s, z)))

    def render(self):
        for obj in self.objects:
            obj.render()