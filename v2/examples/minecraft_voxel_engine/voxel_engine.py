from settings import *
from shader_program import ShaderProgram
from scene import Scene
from player import Player
from textures import Textures
from sound import Mixer
from inventory import Inventory
import moderngl as mgl
import pygame as pg
from array import array
import sys, os, random

class VoxelEngine:
    def __init__(self, withloader=None):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        self.SCREEN = pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'
        
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.gamemode = GameMode.SURVIVAL

        self.is_running = True
        self.finished_processing = False

        self.on_init(withloader)

    def on_init(self, withloader=None):
        self.textures = Textures(self)
        if withloader: withloader("TEXTURES_LOADED")
        self.player = Player(self)
        if withloader: withloader("PLAYER_LOADED")
        self.shader_program = ShaderProgram(self)
        if withloader: withloader("SHADERS_LOADED")
        self.scene = Scene(self)
        if withloader: withloader("TERRAIN_LOADED")
        self.mixer = Mixer(pg)
        if withloader: withloader("SOUNDS_LOADED")
        self.inventory = Inventory(self)
        if withloader: withloader("INVENTORY_LOADED")

        self.finished_processing = True

        @self.mixer.on_event
        def track_finished(instance:self.mixer):
            instance.play_track(random.choice(os.listdir('./sounds/tracks/')))
        
        self.mixer.start_checking("track_finished")
        self.mixer.play_track(random.choice(os.listdir('./sounds/tracks/')))

    def update(self):
        self.player.update()
        self.shader_program.update()
        self.scene.update()

        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def render(self):
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            self.player.handle_event(event=event)

    def run(self, withrunner=None):
        self.SCREEN.set_alpha(1)
        while self.is_running and self.finished_processing:
            self.handle_events()
            self.update()
            self.render()
            if withrunner: withrunner()
            self.SCREEN.set_alpha(0)
        #pg.mixer.stop()
        pg.display.quit()
        self.mixer.stop_all_audio()
        #pg.quit()
        #sys.exit()