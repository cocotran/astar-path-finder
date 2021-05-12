import random

from place import *
from node import *


class Map:
    def __init__(self) -> None:
        self._map: list = []
        self._vertices: list = []
        self._start_point: Node = None
        self._end_point: Node = None

    def generate_vertices(self, width: int, height: int) -> None:
        for i in range((width + 1) * (height + 1)):
            self._vertices.append(Node(str(i)))

    def generate_new_map(self, width: int, height: int):
        for i in range(width * height):
            random_place: int = random.randint(0, 3)
            if random_place == 0:
                self._map.append(QuarantinePlace())
            elif random_place == 1:
                self._map.append(VaccineSpot())
            elif random_place == 2:
                self._map.append(PlayingGround())
            else:
                self._map.append(EmptyPlace())

        for i in range(width * height):
            self._map[i].top_place = self._map[
                i - width] if i - width >= 0 else None
            self._map[i].bottom_place = self._map[
                i + width] if i + width < width * height else None
            self._map[i].left_place = self._map[i -
                                                1] if i % width != 0 else None
            self._map[i].right_place = self._map[i +
                                                 1] if i % width != 2 else None

    def display_map(self, width: int, height: int) -> None:
        for y in range(height):
            for x in range(width):
                print(self._map[y * width + x]._icon, end='   ')
            print("\n")


map = Map()
map.generate_new_map(3, 3)
map.display_map(3, 3)
