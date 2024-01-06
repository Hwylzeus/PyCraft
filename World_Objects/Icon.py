from Settings import *
from Meshes.Hotbar_Icon_Mesh import HotBarIconMesh

class Icon:
    def __init__(self, voxel_handler, voxel_id=1, vertical=0):
        self.app = voxel_handler.app
        self.handler = voxel_handler
        self.icon11 = HotBarIconMesh(self.app, x=0.02, y=-0.02)
        self.icon12 = HotBarIconMesh(self.app, x=0.105, y=-0.02)
        self.icon13 = HotBarIconMesh(self.app, x=0.19, y=-0.02)
        self.icon14 = HotBarIconMesh(self.app, x=0.275, y=-0.02)
        self.icon15 = HotBarIconMesh(self.app, x=0.36, y=-0.02)

        self.icon21 = HotBarIconMesh(self.app, x=0.02, y=-0.17)
        self.icon22 = HotBarIconMesh(self.app, x=0.105, y=-0.17)
        self.icon23 = HotBarIconMesh(self.app, x=0.19, y=-0.17)
        self.icon24 = HotBarIconMesh(self.app, x=0.275, y=-0.17)
        self.icon25 = HotBarIconMesh(self.app, x=0.36, y=-0.17)

        self.icon31 = HotBarIconMesh(self.app, x=0.02, y=-0.32)
        self.icon32 = HotBarIconMesh(self.app, x=0.105, y=-0.32)
        self.icon33 = HotBarIconMesh(self.app, x=0.19, y=-0.32)
        self.icon34 = HotBarIconMesh(self.app, x=0.275, y=-0.32)
        self.icon35 = HotBarIconMesh(self.app, x=0.36, y=-0.32)
        self.icon36 = HotBarIconMesh(self.app, x=0.445, y=-0.32)
        self.icon37 = HotBarIconMesh(self.app, x=0.530, y=-0.32)
        self.icon38 = HotBarIconMesh(self.app, x=0.615, y=-0.32)
        self.icon39 = HotBarIconMesh(self.app, x=0.7, y=-0.32)

        # self.icon41 = HotBarIconMesh1(self.app, x=0.02, y=-0.17)
        # self.icon42 = HotBarIconMesh1(self.app, x=0.105, y=-0.17)
        # self.icon43 = HotBarIconMesh1(self.app, x=0.19, y=-0.17)
        # self.icon44 = HotBarIconMesh1(self.app, x=0.275, y=-0.17)
        # self.icon45 = HotBarIconMesh1(self.app, x=0.36, y=-0.17)

        self.voxel_id = voxel_id;

    def update(self):
        pass

    def render(self):
        self.icon11.program['voxel_id'] = 1
        self.icon11.render()
        self.icon12.program['voxel_id'] = 2
        self.icon12.render()
        self.icon13.program['voxel_id'] = 3
        self.icon13.render()
        self.icon14.program['voxel_id'] = 4
        self.icon14.render()
        self.icon15.program['voxel_id'] = 5
        self.icon15.render()

        self.icon21.program['voxel_id'] = 6
        self.icon21.render()
        self.icon22.program['voxel_id'] = 7
        self.icon22.render()
        self.icon23.program['voxel_id'] = 8
        self.icon23.render()
        self.icon24.program['voxel_id'] = 9
        self.icon24.render()
        self.icon25.program['voxel_id'] = 10
        self.icon25.render()

        self.icon31.program['voxel_id'] = 21
        self.icon31.render()
        self.icon32.program['voxel_id'] = 22
        self.icon32.render()
        self.icon33.program['voxel_id'] = 23
        self.icon33.render()
        self.icon34.program['voxel_id'] = 24
        self.icon34.render()
        self.icon35.program['voxel_id'] = 25
        self.icon35.render()
        self.icon36.program['voxel_id'] = 26
        self.icon36.render()
        self.icon37.program['voxel_id'] = 27
        self.icon37.render()
        self.icon38.program['voxel_id'] = 28
        self.icon38.render()
        self.icon39.program['voxel_id'] = 29
        self.icon39.render()