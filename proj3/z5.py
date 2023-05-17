import proj3.pro3 as p3
import numpy as np

vertices = 8
edges = 12

# 1

graph = p3.random_graph_weights(vertices,edges)
print(graph)

# 5

print(np.array(p3.prim(graph)))


# N: 8 L: 12
# [None, None, 1, None, 5, 9, 1, None]
# [None, None, 8, 5, None, None, None, None]
# [1, 8, None, 6, None, 5, 9, 5]
# [None, 5, 6, None, None, 3, 9, None]
# [5, None, None, None, None, None, None, None]
# [9, None, 5, 3, None, None, None, None]
# [1, None, 9, 9, None, None, None, None]
# [None, None, 5, None, None, None, None, None]

# [[None None 1 None 5 None 1 None]
#  [None None None 5 None None None None]
#  [1 None None None None 5 None 5]
#  [None 5 None None None 3 None None]
#  [5 None None None None None None None]
#  [None None 5 3 None None None None]
#  [1 None None None None None None None]
#  [None None 5 None None None None None]]