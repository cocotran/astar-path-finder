import random
import string

from map.place import *
from map.node import *

# List of names for nodes
NODE_NAME: list = list(string.ascii_uppercase) + list(string.ascii_lowercase)


class Map:
    def __init__(self, height: int, width: int) -> None:
        self.__grids: list = []  # 2 dimensional array
        self.__nodes: list = []  # 1 dimensional array
        self.__width: int = (
            width  # _width: width of the map; _width + 1: number of nodes on each row
        )
        self.__height: int = height  # _height: height of the map; _height + 1: number of nodes on each column

        self.__generate_new_map__()
        self.__generate_vertices__()
        self.__assign_node_neighbors__()
        self.__assign_grid_vertices__()
        self.__set_nodes_neighbors_distance__()

    def __generate_new_map__(self) -> None:
        for i in range(self.__width * self.__height):
            random_place: int = random.randint(0, 5)
            if random_place == 0:
                self.__grids.append(QuarantinePlace())
            elif random_place == 1 or random_place == 2:
                self.__grids.append(VaccineSpot())
            elif random_place == 3 or random_place == 4:
                self.__grids.append(PlayingGround())
            else:
                self.__grids.append(EmptyPlace())
        self.__grids = [
            self.__grids[i : i + self.__width]
            for i in range(0, len(self.__grids), self.__width)
        ]

    def __generate_vertices__(self) -> None:
        for y in range(self.__height + 1):
            for x in range(self.__width + 1):
                index: int = y * (self.__width + 1) + x
                node_name = NODE_NAME[index] if index < len(NODE_NAME) else str(index)
                self.__nodes.append(Node(node_name, float(x), float(y)))

    def __assign_node_neighbors__(self) -> None:
        for i in range((self.__width + 1) * (self.__height + 1)):
            self.__nodes[i].top_node = (
                self.__nodes[i - self.__width - 1]
                if i - self.__width - 1 >= 0
                else None
            )
            self.__nodes[i].bottom_node = (
                self.__nodes[i + self.__width + 1]
                if i + self.__width + 1 < (self.__width + 1) * (self.__height + 1)
                else None
            )
            self.__nodes[i].left_node = (
                self.__nodes[i - 1] if i % (self.__width + 1) != 0 else None
            )
            self.__nodes[i].right_node = (
                self.__nodes[i + 1] if i % (self.__width + 1) != self.__width else None
            )

    def __assign_grid_vertices__(self) -> None:
        for y in range(self.__height + 1):
            for x in range(self.__width + 1):
                self.__nodes[y * (self.__width + 1) + x].top_left_place = (
                    self.__grids[y - 1][x - 1] if y - 1 >= 0 and x - 1 >= 0 else None
                )
                self.__nodes[y * (self.__width + 1) + x].top_right_place = (
                    self.__grids[y - 1][x] if y - 1 >= 0 and x < self.__width else None
                )
                self.__nodes[y * (self.__width + 1) + x].bottom_left_place = (
                    self.__grids[y][x - 1] if x - 1 >= 0 and y < self.__height else None
                )
                self.__nodes[y * (self.__width + 1) + x].bottom_right_place = (
                    self.__grids[y][x]
                    if x < self.__width and y < self.__height
                    else None
                )

    def __set_nodes_neighbors_distance__(self) -> None:
        for i in self.__nodes:
            i.set_neighbors_distance()

    # Function to draw the map to the console
    def __str__(self) -> str:
        print("")
        pre_name: str = ""
        post_name: str = ""
        if len(self.__nodes) > 52:
            pre_name = " "
            post_name = " "

        for y in range(self.__height + 1):

            # Draw nodes
            for x in range(self.__width + 1):
                end_mark: str = "-----" if x != self.__width else "\n"
                node_name: str = self.__nodes[y * (self.__width + 1) + x].name

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
                    print(pre_name + "|" + post_name, end="  ")
                    print(self.__grids[y][x].get_icon(), end="  ")
                    print("|", end="\n") if x == self.__width - 1 else None

        return ""

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_nodes(self) -> list:
        return self.__nodes

    def get_grid_by_index(self, index: int) -> Place:
        column_index: int = index % self.__width
        row_index: int = (index - column_index) / self.__width
        return self.__grids[row_index][column_index]

    def get_node_by_index(self, index: int) -> Node:
        return self.__nodes[index]

    def get_all_quarantine_nodes(self) -> list:
        quarantine_nodes: list = []
        for node in self.__nodes:
            if (
                node.bottom_left_place != None
                and node.bottom_left_place.type == "Quarantine Place"
            ):
                quarantine_nodes.append(node)
        return quarantine_nodes

    def reset_all_node_states(self) -> None:
        for node in self.__nodes:
            node.isVisited = False
            node.global_goal = float("inf")
            node.local_goal = float("inf")
            node.parent = None  # No parents
