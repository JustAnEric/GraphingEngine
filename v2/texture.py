import moderngl as mgl, os, sys, pygame as pg

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture('textures/greengrass.png')
        self.textures[1] = self.get_texture('textures/oak_log.png')
        self.textures[2] = self.get_texture('textures/oak_leaves.png')
        self.textures[3] = self.get_texture('textures/cobblestone.png')
        self.textures[4] = self.get_texture('textures/bummilkshake.png')

    def get_texture(self, path):
        texture = pg.image.load(resource_path(path)).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3, data=pg.image.tostring(texture, 'RGB'))
        #mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        #quality
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]