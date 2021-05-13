import random
import string

from map.place import *
from map.node import *

NODE_NAME: list = list(string.ascii_uppercase) + list(string.ascii_lowercase)

class Map:
    def __init__(self, width: int, height: int) -> None:
        self._map: list = []
        self._vertices: list = []
        self._width = width
        self._height = height
        self._start_point: Node = None
        self._end_point: Node = None

        self._generate_new_map()
        self._generate_vertices()
        self._assign_grid_neighbor()
        self._assign_grid_vertices()
        self.display_map()

    def _generate_vertices(self) -> None:
        for i in range((self._width + 1) * (self._height + 1)):
            node_name = NODE_NAME[i] if i < len(NODE_NAME) else str(i)
            self._vertices.append(Node(node_name)) 
        self._vertices = [self._vertices[i:i + self._width + 1] for i in range(0, len(self._vertices), self._width + 1)]

    def _assign_grid_neighbor(self) -> None:
        for i in range(self._width * self._height):
            self._map[i].top_place = self._map[i - self._width] if i - self._width >= 0 else None
            self._map[i].bottom_place = self._map[i + self._width] if i + self._width < self._width * self._height else None
            self._map[i].left_place = self._map[i - 1] if i % self._width != 0 else None
            self._map[i].right_place = self._map[i + 1] if i % self._width != self._width - 1 else None

    def _assign_grid_vertices(self) -> None:
        for y in range(self._height):
            for x in range(self._width):
                self._map[y * self._width + x].top_left_node = self._vertices[y][x]
                self._map[y * self._width + x].top_right_node = self._vertices[y][x + 1]
                self._map[y * self._width + x].bottom_left_node = self._vertices[y + 1][x]
                self._map[y * self._width + x].bottom_right_node = self._vertices[y + 1][x + 1]

    def _generate_new_map(self) -> None:
        for i in range(self._width * self._height):
            random_place: int = random.randint(0, 3)
            if random_place == 0:
                self._map.append(QuarantinePlace())
            elif random_place == 1:
                self._map.append(VaccineSpot())
            elif random_place == 2:
                self._map.append(PlayingGround())
            else:
                self._map.append(EmptyPlace())

    def display_map(self) -> None:
        for y in range(self._height):
            for i in range(self._width + 1):
                end_mark: str = '-----' if i % (self._width + 1) != self._width else '\n'
                print(self._vertices[y][i]._name, end=end_mark)
            for x in range(self._width):
                print('|', end='  ')
                print(self._map[y * self._width + x].get_icon(), end='  ')
                print('|', end='\n') if x % (self._width) == self._width - 1 else None
        for i in range(self._width + 1):
                end_mark: str = '-----' if i % (self._width + 1) != self._width else '\n'
                print(self._vertices[-1][i]._name, end=end_mark) # Get the last nested list to draw the bottom line of the map 
