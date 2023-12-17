from pygame import Vector2

class Ray:
    def __init__(self, start: Vector2, direction: Vector2) -> None:
        pass


class WorldRay(Ray): #make just one ray in the future, and then have an option to also check if I am counting enemies
    step: int = 0.1
    max_length: int = 50
    def __init__(self, start: Vector2, direction: Vector2, world: list) -> None:
        super().__init__(start, direction)
        self.hit = False
        self.hit_pos = Vector2(start)
        self.length = 0
        while self.hit == False:
            self.hit_pos += direction*0.1
            x = int(self.hit_pos.x)
            y = int(self.hit_pos.y)

            if world[y][x] == 1:
                self.length = (self.hit_pos - start).length()
                break

