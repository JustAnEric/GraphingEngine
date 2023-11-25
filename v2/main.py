from model import *
from camera import Camera
from camera import Player
from light import Light
from mesh import Mesh
from scene import Scene
import moderngl as mgl
import numpy as np
import sys, os, time, signal 
from timecycle import TimeController
import pygame as pg

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainGameWindow():
    def __init__(self) -> None:
        super().__init__()
        self.draw_game()
        #pg.draw.rect(self.game.screen, self.game.inventory_frame_color, self.game.inventory_frame, 500)
        #self.game.screen.fill((0, 0, 0))
        #pg.draw.rect(self.game.screen, self.game.inventory_frame_color, pg.Rect(0, 0, 160, 160))

    def draw_game(self):
        self.game = GraphicsEngine()
        self.game.run()
    
    def update(self):
        self.game.update()

class GraphicsEngine:
    def __init__(self, win_size=(1600,900)):
        pg.init()
        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        self.ctx = mgl.create_context()
        #self.ctx.front_face = 'cw'
        self.ctx.enable(
            flags=mgl.DEPTH_TEST #| mgl.CULL_FACE
        )
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        self.light = Light()
        self.camera = Player(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.timecycle = TimeController(self)

        corners = pg.display.get_window_size()

        self.inventory_frame_color = (255, 255, 255)

        self.timecycle.runs()

    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
    
    def render(self):
        #clear framebuffer
        self.ctx.clear(color=self.timecycle.get_calc_c())
        # render scene
        self.scene.render()
        #swap buffers

        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    
    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(100)

    def update(self):
        self.get_time()
        self.check_events()
        self.camera.update()
        self.render()
        self.delta_time = self.clock.tick(100)

        self.screen.fill((0, 0, 0))

        d = pg.draw.rect(self.screen, self.inventory_frame_color, (0, 0, 160, 160))
        pg.display.update()
    
if __name__ == "__main__":
    app = MainGameWindow()