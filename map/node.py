from map.node import *
from map.place import *


class Node:
    def __init__(self, name: str, x: float, y: float) -> None:
        self.name: str = name
        self.top_node: Node = None
        self.bottom_node: Node = None
        self.left_node: Node = None
        self.right_node: Node = None
        self.top_left_place: Place = None
        self.top_right_place: Place = None
        self.bottom_left_place: Place = None
        self.bottom_right_place: Place = None

        self.__neighbors: dict = {}
        self.x: float = x
        self.y: float = y
        self.parent: Node = None
        self.isVisited: bool = False
        self.global_goal: float = float('inf')
        self.local_goal: float = float('inf')

    def set_neighbors_distance(self) -> None:
        # Top
        if self.top_node != None:
            if self.left_node != None:
                if self.right_node != None:  # Left & Right
                    cost: float = self.top_left_place.get_cost(
                    ) + self.top_right_place.get_cost() / 2
                    self.__neighbors[
                        self.top_node] = cost if cost < 3.0 else float('inf')
                else:  # left & !Right
                    self.__neighbors[
                        self.top_node] = self.top_left_place.get_cost()
            else:  # !Left & Right
                self.__neighbors[
                    self.top_node] = self.top_right_place.get_cost()

        # Bottom
        if self.bottom_node != None:
            if self.left_node != None:
                if self.right_node != None:  # Left & Right
                    cost: float = self.bottom_left_place.get_cost(
                    ) + self.bottom_right_place.get_cost() / 2
                    self.__neighbors[
                        self.bottom_node] = cost if cost < 3.0 else float(
                            'inf')
                else:  # left & !Right
                    self.__neighbors[
                        self.bottom_node] = self.bottom_left_place.get_cost()
            else:  # !Left & Right
                self.__neighbors[
                    self.bottom_node] = self.bottom_right_place.get_cost()

        # Left
        if self.left_node != None:
            if self.top_node != None:
                if self.bottom_node != None:  # Top & Bot
                    cost: float = self.top_left_place.get_cost(
                    ) + self.bottom_left_place.get_cost() / 2
                    self.__neighbors[
                        self.left_node] = cost if cost < 3.0 else float('inf')
                else:  # Top & !Bot
                    self.__neighbors[
                        self.left_node] = self.top_left_place.get_cost()
            else:  # !Top & Bot
                self.__neighbors[
                    self.left_node] = self.bottom_left_place.get_cost()

        # Right
        if self.right_node != None:
            if self.top_node != None:
                if self.bottom_node != None:  # Top & Bot
                    cost: float = self.top_right_place.get_cost(
                    ) + self.bottom_right_place.get_cost() / 2
                    self.__neighbors[
                        self.right_node] = cost if cost < 3.0 else float('inf')
                else:  # Top & !Bot
                    self.__neighbors[
                        self.right_node] = self.top_right_place.get_cost()
            else:  # !Top & Bot
                self.__neighbors[
                    self.right_node] = self.bottom_right_place.get_cost()

    def get_neighbors(self) -> list:
        return self.__neighbors
