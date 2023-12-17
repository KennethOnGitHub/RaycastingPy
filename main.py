import numpy
import pygame
from pygame import Vector2 as Vector2 #I don't like writing pygame.Vector2

SCREEN_SIZE = pygame.Vector2(1380, 720)
RENDER_RES = pygame.Vector2(120, 720)
HORIZONTAL_RRES = int(RENDER_RES.x)
VERTICAL_RRES = int(RENDER_RES.y)
HALF_VERT_RRES = int(VERTICAL_RRES / 2)

FOV = 90

world = [
    [0, 0, 0, 0 , 0],
    [0, 0, 0, 0 ,1],
    [0, 0, 0, 0 ,1],
    [0, 0, 0, 1 ,0],
    [1, 1, 0, 0 ,0],
]

class Player:
    def __init__(self) -> None:
        self.pos:Vector2 = Vector2(1,1)
        self.lookVector:Vector2 = Vector2 (1, -1)

def main():
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)
    SKY_COLOUR = 'blue'
    screen = pygame.display.get_surface()

    player = Player()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        frame = generate_frame(player.pos, player.lookVector)
        
        frame_surface = pygame.surfarray.make_surface(frame)

        screen.fill(SKY_COLOUR)
        screen.blit(frame_surface, (0,0))
        pygame.display.flip()

def generate_frame(playerpos : Vector2, lookvector:Vector2) -> numpy.ndarray:
    camera_plane = lookvector.rotate(90)
    frame = numpy.array([[(100, 100, 100) for y in range(VERTICAL_RRES)] for x in range(HORIZONTAL_RRES)]) 

    for x in range(HORIZONTAL_RRES):
        plane_scalar = -1 + 2*(x/HORIZONTAL_RRES) #smoothly increases from -1 to 1
        ray_vector = lookvector + (camera_plane * plane_scalar) 

        line_height = int(SCREEN_SIZE.y / (raycast(playerpos, ray_vector) + 0.0001)  )
        half_line = int(line_height/2)
        screen_vertical_mid = int(SCREEN_SIZE.y/2)

        frame[x][ screen_vertical_mid - half_line:screen_vertical_mid + half_line] = (100, 0, 0)

    
    return frame

def raycast(startpos:Vector2, step_vector:Vector2, step: int = 0.1, raylength:int = 20) -> int: #currently jusst returns the length of the ray, change this in the future
    checkedPos:Vector2 = startpos
    for count in range(raylength):
        x = int(checkedPos.x)
        y = int(checkedPos.y)

        cell = world[y%5][x%5]

        print(count, x, y, cell)

        if cell == 1:

            return step_vector.length() * step * count
        checkedPos += step_vector * step
    else:
        return None
    



        



    
if __name__ == '__main__':
    main()
