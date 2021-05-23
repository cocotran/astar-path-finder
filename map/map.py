import random
import string

from map.place import *
from map.node import *

# List of names for nodes
NODE_NAME: list = list(string.ascii_uppercase) + list(string.ascii_lowercase)

class Map:
    def __init__(self, width: int, height: int) -> None:
        self.__map: list = []
        self.__vertices: list = []
        self.__width = width # _width: width of the map; _width + 1: number of nodes on each row
        self.__height = height # _height: height of the map; _height + 1: number of nodes on each column

        self.__generate_new_map__()
        self.__generate_vertices__()
        self.__assign_node_neighbors__()
        self.__assign_grid_vertices__()
        self.__set_nodes_neighbors_distance__()

    def __generate_new_map__(self) -> None:
        for i in range(self.__width * self.__height):
            random_place: int = random.randint(0, 3)
            if random_place == 0:
                self.__map.append(QuarantinePlace())
            elif random_place == 1:
                self.__map.append(VaccineSpot())
            elif random_place == 2:
                self.__map.append(PlayingGround())
            else:
                self.__map.append(EmptyPlace())
        self.__map = [self.__map[i:i + self.__width] for i in range(0, len(self.__map), self.__width)]

    def __generate_vertices__(self) -> None:
        for y in range(self.__height + 1):
            for x in range(self.__width + 1):
                index: int = y * (self.__width + 1) + x
                node_name = NODE_NAME[index] if index < len(NODE_NAME) else str(index)
                self.__vertices.append(Node(node_name, float(x), float(y))) 

    def __assign_node_neighbors__(self) -> None:
        for i in range((self.__width + 1) * (self.__height + 1)):
            self.__vertices[i].top_node = self.__vertices[i - self.__width - 1] if i - self.__width - 1 >= 0 else None
            self.__vertices[i].bottom_node = self.__vertices[i + self.__width + 1] if i + self.__width + 1 < (self.__width + 1) * (self.__height + 1) else None
            self.__vertices[i].left_node = self.__vertices[i - 1] if i % (self.__width + 1) != 0 else None
            self.__vertices[i].right_node = self.__vertices[i + 1] if i % (self.__width + 1) != self.__width else None

    def __assign_grid_vertices__(self) -> None:
        for y in range(self.__height + 1):
            for x in range(self.__width + 1):
                self.__vertices[y * (self.__width + 1) + x].top_left_place = self.__map[y - 1][x - 1] if y - 1 >= 0 and x - 1 >= 0 else None
                self.__vertices[y * (self.__width + 1) + x].top_right_place = self.__map[y - 1][x] if y - 1 >= 0 and x < self.__width else None
                self.__vertices[y * (self.__width + 1) + x].bottom_left_place = self.__map[y][x - 1] if x - 1 >= 0 and y < self.__height else None
                self.__vertices[y * (self.__width + 1) + x].bottom_right_place = self.__map[y][x] if x < self.__width and y < self.__height else None

    def __set_nodes_neighbors_distance__(self) -> None:
        for i in self.__vertices:
            i.set_neighbors_distance()

    def get_vertices(self) -> list:
        return self.__vertices

    # Function to draw the map to the console
    def display_map(self) -> None:
        pre_name: str = ""
        post_name: str = ""
        if len(self.__vertices) > 52:
            pre_name = " "
            post_name = " "

        for y in range(self.__height + 1):

            # Draw nodes
            for x in range(self.__width + 1):
                end_mark: str = '-----' if x != self.__width else '\n'
                node_name: str = self.__vertices[y * (self.__width + 1) + x].name
                if node_name.isalpha():
                    if x != self.__width:
                        print(pre_name + node_name + post_name, end=end_mark) 
                    else:
                        print(node_name, end=end_mark)
                else:
                    if len(node_name) == 2:
                        print(node_name + post_name, end=end_mark)
                    else:
                        print(node_name, end=end_mark)

            # Draw grids
            for x in range(self.__width):
                if y < self.__height:
                    print(pre_name + '|' + post_name, end='  ')
                    print(self.__map[y][x].get_icon(), end='  ')
                    print('|', end='\n') if x == self.__width - 1 else None

    