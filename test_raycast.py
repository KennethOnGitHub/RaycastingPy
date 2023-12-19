import unittest
import raycast
from pygame import Vector2

class TestRay(unittest.TestCase):
    def test_ray_in_corridor(self):
        world = [[0,0,0,0,0,0,1]]

        testray = raycast.WorldRay(Vector2(0,0), Vector2(1,0), world)

        #self.assertTrue(testray.hit_pos.x > 6 and testray.hit_pos.x < 7)
        self.assertEqual(testray.length, 6)

    def test_ray_going_diagonal(self):
        world = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
        ]


        testray = raycast.WorldRay(Vector2(0,0), Vector2(1,1).normalize(), world)

        self.assertTrue(4.1 < testray.length < 4.4)

if __name__ == '__main__':
    unittest.main()