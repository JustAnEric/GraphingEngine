import moderngl as mgl, pygame as pg, numpy as np, glm, random, os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

inc_sbm, increm_sbm = 2, (2,2,2)

class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0,0,0), rot=(0,0,0), scale=(1,1,1), identifier:int=0):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera
        self.identifier = identifier
    
    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1,0,0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0,1,0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0,0,1))
        # scaling
        m_model = glm.scale(m_model, self.scale)

        return m_model
    
    def render(self):
        self.update()
        self.vao.render()
    
class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0,0,0), rot=(0,0,0), scale=(1,1,1), identifier:int=0):
        super().__init__(app, vao_name, tex_id, pos, rot, scale, identifier)
        self.on_init()
    
    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
    
    def on_init(self):
        #texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        #mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        #light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class BumMilkshake(Cube):
    def __init__(self, app, pos=(0,0,0), rot=(0,0,0)):
        super().__init__(app, 'bum-milkshake', 4, pos=pos, rot=rot, scale=(1,1,1), identifier=random.randint(0,100000000000000000000000000000000000))

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
    
    def on_init(self):
        #texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        #mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        #light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

    def rotate(self, angle=(0,0,0)):
        self.rot = glm.vec3([glm.radians(a) for a in angle])
        self.get_model_matrix()
        return

    def move(self, pos=(0,0,0)):
        self.pos = pos
        self.get_model_matrix()
        return