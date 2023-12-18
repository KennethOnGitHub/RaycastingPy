from pygame import Vector2
import math

class Ray:
    def __init__(self, start: Vector2, direction: Vector2) -> None:
        pass


class WorldRay(Ray): #make just one ray in the future, and then have an option to also check if I am counting enemies
    step: int = 0.1
    max_length: int = 50
    def __init__(self, start: Vector2, direction: Vector2, world: list) -> None:
        super().__init__(start, direction)
        self.hit = False
        self.length = 0

        map_coords = Vector2(int(start.x), int(start.y))
        map_step = Vector2(0,0)

        dydx_squared = (direction.y * direction.y)/(direction.x * direction.x) if direction.x != 0 else 999_999_999
        dxdy_squared = (direction.x * direction.x)/(direction.y * direction.y) if direction.y != 0 else 999_999_999
        

        ray_step_length = Vector2(math.sqrt(1 + dydx_squared), math.sqrt(1 + dxdy_squared)) #the distance a ray has to travel to step by one x coordinate/y coordinate

        ray_length = Vector2(0,0)#a little odd use of vectors, but the x component represents the length of the x ray and the y component is the length of the y ray.

        if direction.x < 0:
            map_step.x = -1
            x_difference_to_edge = (start.x - map_coords.x)
        else:
            map_step.x = 1
            x_difference_to_edge = (1 - start.x + map_coords.x)
        ray_length.x = x_difference_to_edge * ray_step_length.x

        if direction.y < 0:
            map_step.y = -1
            y_difference_to_edge = (start.y - map_coords.y)
        else:
            map_step.y = 1
            y_difference_to_edge = (1 - start.y + map_coords.y)
        ray_length.y = y_difference_to_edge * ray_step_length.y

        while self.hit == False:
            if ray_length.x < ray_length.y:
                map_coords.x += map_step.x
                ray_length.x += ray_step_length.x
                self.length = ray_length.x
            else:
                map_coords.x += map_step.y
                ray_length.y += ray_step_length.y
                self.length = ray_length.y
        
            if world[int(map_coords.y)][int(map_coords.x)]:
                self.hit = True

        

        # while self.hit == False:
        #     self.hit_pos += direction*0.1
        #     x = int(self.hit_pos.x)
        #     y = int(self.hit_pos.y)

        #     if world[y][x] >= 1:
        #         self.length = (self.hit_pos - start).length()
        #         break

