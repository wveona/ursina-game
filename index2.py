from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from pynput.keyboard import Key

app = Ursina()

#택스쳐
sky_texture   = load_texture('assets/skybox.png')
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')

ui =[
    load_texture('assets/grass_block.png'), 
    load_texture('assets/grass_block.png'), 
    load_texture('assets/stone_block.png'), 
    load_texture('assets/brick_block.png') 
] 

grass_ui = load_texture('assets/grass_block_ui.png')
stone_ui = load_texture('assets/stone_block_ui.png')
brick_ui = load_texture('assets/brick_block_ui.png')

block_pick = 1
h_ui = 1

def input(key):
    global h_ui, hand
    if key.isdigit():
        h_ui = int(key)
        if h_ui >= len(ui):
            h_ui = len(ui) - 1
        hand.texture = ui[h_ui]
    if key == "escape":
        quit()


#블록 고르기
def update():
    global block_pick
    
    if held_keys['1']: block_pick = 1 
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

    
   
 

#블록
class Voxel(Button):
    def __init__(self, position =(0,0,0),texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.light_gray,
            scale = 0.5)

    #블록 설치,삭제
    def input(self,key):
        if self.hovered:
            if key =='right mouse down':
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal,texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal,texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal,texture=brick_texture)

            if key == 'left mouse down':
                destroy(self)
#하늘
class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

#손
hand = Entity( 
    parent =camera.ui,
    model ='assets/block',
    texture = ui[h_ui],
    scale =0.2,
    rotation=Vec3(-10,-10,10),
    position=Vec2(0.6,-0.6)
)
            
    
    
    



#핫바
class hotbar(Entity):
	def __init__(self,position =(0,-0.47)):
		super().__init__(
            parent=camera.ui,
            model = 'quad',
            scale_y=0.08,
            scale_x=0.8,
            position = position,
            color=color.dark_gray                 
        )

#핫바 잔디
class Grid(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model = 'quad',
            scale_y=0.06,
            scale_x=0.06,
            position = (-0.335,-0.465),
            texture = grass_ui,
            texture_scale =(9,1)

        )


#핫바 돌
class Grid2(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model = 'quad',
            scale_y=0.06,
            scale_x=0.06,
            position = (-0.25,-0.465),
            texture = stone_ui,
            texture_scale =(9,1)

        )


#핫바 돌
class Grid3(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model = 'quad',
            scale_y=0.06,
            scale_x=0.06,
            position = (-0.165,-0.465),
            texture = brick_ui,
            texture_scale =(9,1)

        )
        
        



for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky()
hotbar = hotbar()
grid = Grid()
grid = Grid2()
grid = Grid3()
app.run()


