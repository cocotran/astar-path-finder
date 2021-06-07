from map.node import Node
from map.map import *


def print_path(path: list) -> None:
    if len(path) > 0:
        print("Path: ", end="")
        print('\033[92m' + path[-1].name + '\033[0m', end=' --> ')
        for i in range(len(path) - 2, 1, -1):
            print(path[i].name + " --> ", end="")
        print('\033[93m' + path[1].name + '\033[0m') if path[1].name != None else None


# The heuristic function estimates the cost to reach goal from node n.
# This implmentation uses Manhattan Distance Heuristic
def a_star(start_node: Node, stop_node: Node) -> tuple:
    def get_Manhattan_Distance_Heuristic(current_node: Node, end_node: Node) -> float:
        distance: float = abs(current_node.x - end_node.x) + abs(
            current_node.y - end_node.y
        )
        return distance

    def get_path(end_node: Node) -> list:
        path: list = [end_node]
        if end_node != None:
            node_pointer: Node = end_node
            while node_pointer.parent != None:
                path.insert(0, node_pointer.parent)

                # Set next node to this node's parent
                node_pointer = node_pointer.parent
        return path

    def get_cost(path: list) -> float:
        cost: float = 0.0
        for i in range(len(path) - 1):  # path is a list of nodes
            neighbors: dict = path[i].get_neighbors()
            cost += neighbors[path[i + 1]]
        return cost

    """THE DIVINE FUNCTION: F = G + H"""

    # Setup starting conditions
    current_node: Node = start_node
    start_node.local_goal = 0.0
    start_node.global_goal = get_Manhattan_Distance_Heuristic(start_node, stop_node)

    # Add start node to not tested list - this will ensure it gets tested.
    # As the algorithm progresses, newly discovered nodes get added to this
    # list, and will themselves be tested later
    not_tested_nodes: list = []
    not_tested_nodes.append(start_node)

    while len(not_tested_nodes) != 0:

        # Sort untested nodes by global goal, lowest to highest
        not_tested_nodes.sort(key=lambda node: node.global_goal)

        # Front of not_tested_nodes is potentially the lowest distance node
        # Remove nodes that have been visited
        # print(not_tested_nodes[0].name + " " + str(not_tested_nodes[0].isVisited))
        if len(not_tested_nodes) != 0 and not_tested_nodes[0].isVisited:
            not_tested_nodes.pop(0)

        # If there are no valid nodes left to test
        if len(not_tested_nodes) == 0:
            break

        current_node = not_tested_nodes[0]
        current_node.isVisited = True  # Only explore a node once

        # Check each of this node's neighbors
        neighbors: dict = current_node.get_neighbors()
        for neighbor_node in neighbors.keys():

            # Only if the neighbor is not visited, add it to not_tested list
            if not neighbor_node.isVisited:
                not_tested_nodes.append(neighbor_node)

            # Calculate the neighbors potential lowest parent distance
            possibly_lower_goal: float = (
                current_node.local_goal + neighbors[neighbor_node]
            )

            # If choosing to path through this node is a lower distance than what
            # the neighbour currently has set, update the neighbour to use this node
            # as the path source, and set its distance scores as necessary
            if possibly_lower_goal < neighbor_node.local_goal:
                neighbor_node.parent = current_node
                neighbor_node.local_goal = possibly_lower_goal

                # The best path length to the neighbour being tested has changed, so
                # update the neighbour's score. The heuristic is used to globally bias
                # the path algorithm, so it knows if its getting better or worse. At some
                # point the algo will realise this path is worse and abandon it, and then go
                # and search along the next best path.
                neighbor_node.globaL_goal = (
                    neighbor_node.local_goal
                    + get_Manhattan_Distance_Heuristic(neighbor_node, stop_node)
                )

    path: list = get_path(stop_node)
    cost: float = get_cost(path)

    return cost, path
