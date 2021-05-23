from map.map import *
from algorithm.astar import *

if __name__ == '__main__':
    map = Map(5, 5)
    map.display_map()
    graph_nodes: dict = map.get_vertices()
    a_star(graph_nodes[0], graph_nodes[-1])
