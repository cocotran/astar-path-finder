from map.node import *
from map.place import *

class Node:
    def __init__(self, name: str, x: float, y: float) -> None:
        self._name: str = name
        self.top_node: Node = None
        self.bottom_node: Node = None
        self.left_node: Node = None
        self.right_node: Node = None
        self.top_left_place: Place = None
        self.top_right_place: Place = None
        self.bottom_left_place: Place = None
        self.bottom_right_place: Place = None

        self._neighbors: dict = {}
        self.x: float = x
        self.y: float = y
        self.g: float = 0.0
        self.h: float = 0.0

    @staticmethod
    def getManhattanDistanceHeuristic(current_node, end_node) -> float:
        distance: float = abs(current_node.x - end_node.x) + abs(current_node.y - end_node.y)
        return distance