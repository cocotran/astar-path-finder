from map.node import *
from map.place import *

class Node:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._moves: dict = {}
        self.top_node: Node = None
        self.bottom_node: Node = None
        self.left_node: Node = None
        self.right_node: Node = None
        self.top_left_place: Place = None
        self.top_right_place: Place = None
        self.bottom_left_place: Place = None
        self.bottom_right_place: Place = None