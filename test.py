from map import node
from map.map import *
from algorithm.astar import *

map = Map(2, 2)
map.display_map()

start = map._Map__vertices[0]
end = map._Map__vertices[-1]

assert start.x == 0.0
assert start.y == 0.0
assert end.x == 2.0
assert end.x == 2.0

# assert Node.getManhattanDistanceHeuristic(start, end) == 4.0
# assert Node.getManhattanDistanceHeuristic(map._Map__vertices[4], end) == 2.0

# start.setManhattanDistanceHeuristic(end)
# assert start.h ==  4.0

node_c: Node = map._Map__vertices[2] 
assert node_c.top_node == None 
assert node_c.bottom_node.name == "F"
assert node_c.left_node.name == "B"
assert node_c.right_node == None

node_e: Node = map._Map__vertices[4]
assert node_e.top_node.name == "B" 
assert node_e.bottom_node.name == "H"
assert node_e.left_node.name == "D"
assert node_e.right_node.name == "F"

assert node_c.top_left_place == None
assert node_c.top_right_place == None
assert node_c.bottom_right_place == None

graph_nodes: dict = map.get_vertices()

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

a_star(graph_nodes[0], graph_nodes[-1])

print("All tests passed")