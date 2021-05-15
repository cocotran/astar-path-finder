from map.node import Node


# The heuristic function estimates the cost to reach goal from node n.
# This implmentation uses Manhattan Distance Heuristic
def a_star(start_node: Node, end_node: Node, heuristic_func: function):

    def reconstruct_path(came_from: Node, current_node: Node) -> list:
        total_path: list = [current_node]
        while current_node in came_from.keys():
            current_node = came_from[current_node]
            total_path.insert(0, current_node) # Prepend current node
        return total_path

    # Main A* algorithm 
    _open_set: list = [start_node]

    # For node n, came_from[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    _came_from: list = []
    
    # For node n, g_core[n] is the cost of the cheapest path from start to n currently known.
    _g_score: list = []
    _g_score[start_node] = 0

    # For node n, f_score[n] := g_score[n] + heuristic_func(n). f_score[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    _f_score: list = []
    _f_score[start_node] = heuristic_func(start_node, end_node)

    while len(_open_set) > 0:
        _current_node: Node = None


    pass