from settings import *
from frustum import Frustum
import time


class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.up = glm.vec3(0,1,0)
        self.right = glm.vec3(1,0,0)
        self.forward = glm.vec3(0,0,-1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

        self.jumping = False

        self.frustum = Frustum(self)

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

    def update_vectors(self):
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0,1,0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        self.position -= self.right * velocity
    
    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
        self.position += self.up * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity

    def move_forward(self, velocity):
        self.position += self.forward * velocity

    def move_back(self, velocity):
        self.position -= self.forward * velocity
    
    def jump(self):
        if self.jumping: return
        self.jumping = True
        for i in range(0, 10, 5):
            time.sleep(0.05)
            self.position += self.up * (i/13)
        time.sleep(0.2)
        for i in range(0, 10, 5):
            time.sleep(0.2)
            self.position -= self.up * (i/13)
        self.jumping = False
    
    def gravity_(self):
        if self.jumping: return
        print(self.position)
        voxel_handler = self.app.scene.world.voxel_handler
        #voxel_handler.chunk.voxels[voxel_handler.get_voxel_id()]
        vp = voxel_handler.get_voxel_below_player(self.position) # voxel pos
        print(vp)
        #self.position.y = vp[2][1]+2
        
