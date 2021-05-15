from map.map import *

map = Map(2, 2)

current = map._vertices[0]
end = map._vertices[-1]

assert current.x == 0.0
assert current.y == 0.0
assert end.x == 2.0
assert end.x == 2.0

assert Node.getManhattanDistanceHeuristic(current, end) == 4.0
assert Node.getManhattanDistanceHeuristic(map._vertices[4], end) == 2.0

print("All tests passed")