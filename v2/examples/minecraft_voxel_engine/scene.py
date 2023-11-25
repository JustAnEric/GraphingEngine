from settings import *
from world import World
import moderngl as mgl
from world_objects.voxel_marker import VoxelMarker
from world_objects.water import Water
from world_objects.clouds import Clouds

class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.voxel_marker = VoxelMarker(self.world.voxel_handler)
        self.water = Water(self.app)
        self.clouds = Clouds(self.app)

    def update(self):
        self.world.update()
        self.voxel_marker.update()
        self.clouds.update()
        

    def render(self):
        self.world.render()
        # rendering without cull face
        self.app.ctx.disable(mgl.CULL_FACE)
        self.clouds.render()
        self.water.render()
        self.app.ctx.enable(mgl.CULL_FACE)

        self.voxel_marker.render()