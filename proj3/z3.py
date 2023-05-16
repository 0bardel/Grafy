import proj3.pro3 as p3
import numpy as np

vertices = 4
edges = 5

# 1

graph = p3.random_graph_weights(vertices,edges)
print(graph)

# 3

distances = {}
for start in range(vertices):
    distances[start] = p3.dijkstra(graph,start=start,verbose=False)
distance_matrix = np.zeros((vertices,vertices))

for i in range(vertices):
    for j in range(vertices):
        if i<j:
            distance_matrix[i][j] = distances[i][j]
            distance_matrix[j][i] = distances[i][j]
            
print(distance_matrix)
