import proj3.pro3 as p3
import numpy as np

vertices = 4
edges = 5

# 1

graph = p3.random_graph_weights(vertices,edges)
print(graph)

# 5

print(np.array(p3.prim(graph)))
