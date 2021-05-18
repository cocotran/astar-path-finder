from map import node
from map.map import *

map = Map(2, 2)
map.display_map()

start = map._Map__vertices[0]
end = map._Map__vertices[-1]

assert start._Node__x == 0.0
assert start._Node__y == 0.0
assert end._Node__x == 2.0
assert end._Node__x == 2.0

assert Node.getManhattanDistanceHeuristic(start, end) == 4.0
assert Node.getManhattanDistanceHeuristic(map._Map__vertices[4], end) == 2.0

start.setManhattanDistanceHeuristic(end)
assert start.h ==  4.0

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

for i in map._Map__vertices:
    i.setNeighbors()

neighbors: dict = start.getNeighbors()
# for i in neighbors:
#     for j in i.keys():
#         print(j.name + ": " + str(i[j]))

neighbors: dict = node_e.getNeighbors()
# for i in neighbors:
#     for j in i.keys():
#         print(j.name + ": " + str(i[j]))

print("All tests passed")