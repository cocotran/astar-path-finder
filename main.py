from typing import List
from algorithm import astar
from map.map import *
from algorithm.astar import *

import enum
import math


class Grid(enum.Enum):
    WIDTH = 0.1
    LENGTH = 0.2


def get_node_index(point_coordinate: tuple, map_width: int) -> int:
    x_coordinate: float = point_coordinate[0]
    y_coordinate: float = point_coordinate[1]

    column_index: float = x_coordinate / Grid.LENGTH.value  # x-coordinate
    row_index: float = y_coordinate / Grid.WIDTH.value  # y-coordinate

    if x_coordinate % Grid.LENGTH.value == 0 and y_coordinate % Grid.WIDTH.value == 0:  # Perfectly on a corner, no need to transfer it.
        pass
    else:  # On the edge or inside the grid
        column_index = math.ceil(column_index)
        row_index = math.floor(row_index)

    return int(row_index * (map_width + 1) + column_index)


def is_within_boundary(map_width: int, map_height: int,
                       point_coordinate: tuple) -> bool:
    x_coordinate: float = point_coordinate[0]
    y_coordinate: float = point_coordinate[1]

    if x_coordinate < 0 or y_coordinate < 0:
        return False

    return x_coordinate <= map_width * Grid.LENGTH.value and y_coordinate <= map_height * Grid.WIDTH.value


def validate_start_end_point(map: Map, start_coordinate: tuple,
                             end_coordinate: tuple) -> bool:
    start_node_index: int = get_node_index(start_coordinate, map.get_width())
    end_node_index: int = get_node_index(end_coordinate, map.get_width())

    if not (is_within_boundary(map.get_width(), map.get_height(),
                               start_coordinate)
            and is_within_boundary(map.get_width(), map.get_height(),
                                   end_coordinate)):
        print('No path is found. Please try again!')
        return False

    if start_node_index == end_node_index:
        print('Already at the destination.')
        return False

    return True


def get_start_end_point() -> tuple:
    start_point: tuple(float) = eval(
        input("Enter start point coordinate (x, y) (e.g., 0.4, 0.15): "))
    end_point: tuple(float) = eval(
        input("Enter start point coordinate (x, y) (e.g., 0.4, 0.15): "))
    return start_point, end_point


def find_path() -> None:
    dimension: tuple(int) = input(
        "Enter map dimension (row x column) (e.g., 3 x 4): ").replace(
            " ", "").split("x")

    map: Map = Map(int(dimension[0]), int(dimension[1]))
    print(map)

    start_point, end_point = get_start_end_point()

    if validate_start_end_point(map, start_point, end_point):
        start_node_index: int = get_node_index(start_point, map.get_width())
        end_node_index: int = get_node_index(end_point, map.get_width())

        start_node: Node = map.get_node_by_index(start_node_index)
        end_node: Node = map.get_node_by_index(end_node_index)

        a_star(start_node, end_node)


if __name__ == '__main__':
    find_path()
