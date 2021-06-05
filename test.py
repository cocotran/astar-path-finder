from map import node
from map.map import *
from algorithm.astar import *
from main import *

map = Map(2, 2)
print(map)

start = map._Map__nodes[0]
end = map._Map__nodes[-1]

assert start.x == 0.0
assert start.y == 0.0
assert end.x == 2.0
assert end.x == 2.0

# assert Node.getManhattanDistanceHeuristic(start, end) == 4.0
# assert Node.getManhattanDistanceHeuristic(map._Map__vertices[4], end) == 2.0

# start.setManhattanDistanceHeuristic(end)
# assert start.h ==  4.0

node_c: Node = map._Map__nodes[2]
assert node_c.top_node == None
assert node_c.bottom_node.name == "F"
assert node_c.left_node.name == "B"
assert node_c.right_node == None

node_e: Node = map._Map__nodes[4]
assert node_e.top_node.name == "B"
assert node_e.bottom_node.name == "H"
assert node_e.left_node.name == "D"
assert node_e.right_node.name == "F"

assert node_c.top_left_place == None
assert node_c.top_right_place == None
assert node_c.bottom_right_place == None

graph_nodes: dict = map.get_nodes()

neighbors: dict = start.get_neighbors()
# for i in neighbors:
#     for j in i.keys():
#         print(j.name + ": " + str(i[j]))

neighbors: dict = node_e.get_neighbors()
# for i in neighbors:
#     for j in i.keys():
#         print(j.name + ": " + str(i[j]))

test_list: list = []
node_1: Node = Node("1", 0, 0)
node_1.global_goal = 1.0
node_2: Node = Node("2", 0, 0)
node_2.global_goal = 2.0
node_3: Node = Node("3", 0, 0)
node_3.global_goal = 3.0
test_list.append(node_3)
test_list.append(node_1)
test_list.append(node_2)
test_list.sort(key=lambda node: node.global_goal)
assert test_list[0] == node_1
assert test_list[1] == node_2
assert test_list[2] == node_3

assert get_node_index((0, 0), 2) == 0
assert get_node_index((0, 0.05), 2) == 0
assert get_node_index((0, 0.15), 2) == 3
assert get_node_index((0.1, 0.2), 2) == 7
assert get_node_index((0.15, 0.15), 2) == 4
assert get_node_index((0.2, 0.1), 2) == 4
assert get_node_index((0.3, 0.0), 2) == 2
assert get_node_index((0.3, 0.15), 2) == 5

assert is_within_boundary(2, 2, (0, 0)) == True
assert is_within_boundary(2, 2, (0.1, 0.2)) == True
assert is_within_boundary(2, 2, (0.4, 0.1)) == True
assert is_within_boundary(2, 2, (0.3, 0.15)) == True
assert is_within_boundary(2, 2, (0.15, 0.3)) == False
assert is_within_boundary(2, 2, (0.5, 0.1)) == False
assert is_within_boundary(2, 2, (-1, 0.1)) == False
assert is_within_boundary(2, 2, (0.3, -0.1)) == False

assert validate_start_end_point(map, (0, 0), (0.4, 0.1)) == True
assert validate_start_end_point(map, (-1, 0), (0.4, 0.1)) == False
assert validate_start_end_point(map, (0, 0), (0.5, 0.1)) == False
assert validate_start_end_point(map, (0.1, 0.2), (0.3, 0.15)) == True

# a_star(graph_nodes[0], graph_nodes[-1])

print("All tests passed")
