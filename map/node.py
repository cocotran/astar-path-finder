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

        self.__neighbors: list = []
        self.__x: float = x
        self.__y: float = y
        self.f: float = 0.0
        self.g: float = 0.0
        self.h: float = 0.0

    def setManhattanDistanceHeuristic(self, end_node) -> None:
        self.h = abs(self.__x - end_node.__x) + abs(self.__y - end_node.__y)

    @staticmethod
    def getManhattanDistanceHeuristic(current_node, end_node) -> float:
        distance: float = abs(current_node.__x - end_node.__x) + abs(current_node.__y - end_node.__y)
        return distance

    def setNeighbors(self) -> None:
        # Top
        if self.top_node != None:
            if self.left_node != None:
                if self.right_node != None: # Left & Right
                    self.__neighbors.append({self.top_node: (self.top_left_place.get_cost() + self.top_right_place.get_cost()) / 2})
                else: # left & !Right
                    self.__neighbors.append({self.top_node: self.top_left_place.get_cost()})
            else: # !Left & Right
                self.__neighbors.append({self.top_node: self.top_right_place.get_cost()})

        # Bottom
        if self.bottom_node != None:
            if self.left_node != None:
                if self.right_node != None: # Left & Right
                    self.__neighbors.append({self.bottom_node: (self.bottom_left_place.get_cost() + self.bottom_right_place.get_cost()) / 2})
                else: # left & !Right
                    self.__neighbors.append({self.bottom_node: self.bottom_left_place.get_cost()})
            else: # !Left & Right
                self.__neighbors.append({self.bottom_node: self.bottom_right_place.get_cost()})

        # Left
        if self.left_node != None:
            if self.top_node != None:
                if self.bottom_node != None: # Top & Bot
                    self.__neighbors.append({self.left_node: (self.top_left_place.get_cost() + self.bottom_left_place.get_cost()) / 2})
                else: # Top & !Bot
                    self.__neighbors.append({self.left_node: self.top_left_place.get_cost()})
            else: # !Top & Bot
                self.__neighbors.append({self.left_node: self.bottom_left_place.get_cost()})
            
        # Right
        if self.right_node != None:
            if self.top_node != None:
                if self.bottom_node != None: # Top & Bot
                    self.__neighbors.append({self.right_node: (self.top_right_place.get_cost() + self.bottom_right_place.get_cost()) / 2})
                else: # Top & !Bot
                    self.__neighbors.append({self.right_node: self.top_right_place.get_cost()})
            else: # !Top & Bot
                self.__neighbors.append({self.right_node: self.bottom_right_place.get_cost()})

    def getNeighbors(self) -> list:
        return self.__neighbors