import random
import string

from map.place import *
from map.node import *

NODE_NAME: list = list(string.ascii_uppercase) + list(string.ascii_lowercase)

class Map:
    def __init__(self, width: int, height: int) -> None:
        self._map: list = []
        self._vertices: list = []
        self._width = width # _width: width of the map; _width + 1: number of nodes on each row
        self._height = height # _height: height of the map; _height + 1: number of nodes on each column
        self._start_point: Node = None
        self._end_point: Node = None

        self._generate_new_map()
        self._generate_vertices()
        self._assign_node_neighbor()
        self._assign_grid_vertices()
        self.display_map()

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
        self._map = [self._map[i:i + self._width] for i in range(0, len(self._map), self._width)]

    def _generate_vertices(self) -> None:
        for i in range((self._width + 1) * (self._height + 1)):
            node_name = NODE_NAME[i] if i < len(NODE_NAME) else str(i)
            self._vertices.append(Node(node_name)) 

    def _assign_node_neighbor(self) -> None:
        for i in range((self._width + 1) * (self._height + 1)):
            self._vertices[i].top_node = self._vertices[i - self._width - 1] if i - self._width - 1 >= 0 else None
            self._vertices[i].bottom_node = self._vertices[i + self._width + 1] if i + self._width + 1 < (self._width + 1) * (self._height + 1) else None
            self._vertices[i].left_node = self._vertices[i - 1] if i % (self._width + 1) != 0 else None
            self._vertices[i].right_node = self._vertices[i + 1] if i % (self._width + 1) != self._width else None

    def _assign_grid_vertices(self) -> None:
        for y in range(self._height + 1):
            for x in range(self._width + 1):
                self._vertices[y * self._width + x].top_left_place = self._map[y - 1][x - 1] if y - 1 >= 0 and x - 1 >= 0 else None
                self._vertices[y * self._width + x].top_right_place = self._map[y - 1][x] if y - 1 >= 0 and x < self._width else None
                self._vertices[y * self._width + x].bottom_left_place = self._map[y][x - 1] if x - 1 >= 0 and y < self._height else None
                self._vertices[y * self._width + x].bottom_right_place = self._map[y][x] if x < self._width and y < self._height else None

    def display_map(self) -> None:
        for y in range(self._height + 1):

            # Draw nodes
            for x in range(self._width + 1):
                end_mark: str = '-----' if x != self._width else '\n'
                print(self._vertices[y * (self._width + 1) + x]._name, end=end_mark)

            # Draw grids
            for x in range(self._width):
                if y < self._height:
                    print('|', end='  ')
                    print(self._map[y][x].get_icon(), end='  ')
                    print('|', end='\n') if x == self._width - 1 else None
