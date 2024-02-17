import pygame as pg
from settings import *
from threading import Thread



class Inventory:
    def __init__(self, app):
        self.app = app
        self.main_inv = [
            1,2,3,4,5,6,7,8,0
        ]

        self.inv_slot = 0

    def keyboard_control(self):
        ks = pg.key.get_pressed()

        if ks[pg.K_1]:
            self.inv_slot = 1
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_2]:
            self.inv_slot = 2
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_3]:
            self.inv_slot = 3
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_4]:
            self.inv_slot = 4
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_5]:
            self.inv_slot = 5
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_6]:
            self.inv_slot = 6
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_7]:
            self.inv_slot = 7
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_8]:
            self.inv_slot = 8
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]
        if ks[pg.K_9]:
            self.inv_slot = 9
            self.app.scene.world.voxel_handler.new_voxel_id = self.main_inv[self.inv_slot]