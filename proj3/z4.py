import proj3.pro3 as p3
import numpy as np

vertices = 8
edges = 12

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

#4

print('centrum grafu', np.argmin(np.sum(distance_matrix,axis=0)))
print('centrum minimax', np.argmin(np.max(distance_matrix,axis=0)))

# N: 8 L: 12
# [None, None, None, 9, 6, None, 7, None]
# [None, None, None, None, 2, 5, 5, None]
# [None, None, None, None, 2, None, 10, None]
# [9, None, None, None, 8, None, None, None]
# [6, 2, 2, 8, None, 9, None, None]
# [None, 5, None, None, 9, None, 3, 5]
# [7, 5, 10, None, None, 3, None, None]
# [None, None, None, None, None, 5, None, None]

# [[ 0.  8.  8.  9.  6. 10.  7. 15.]
#  [ 8.  0.  4. 10.  2.  5.  5. 10.]
#  [ 8.  4.  0. 10.  2.  9.  9. 14.]
#  [ 9. 10. 10.  0.  8. 15. 15. 20.]
#  [ 6.  2.  2.  8.  0.  7.  7. 12.]
#  [10.  5.  9. 15.  7.  0.  3.  5.]
#  [ 7.  5.  9. 15.  7.  3.  0.  8.]
#  [15. 10. 14. 20. 12.  5.  8.  0.]]
# centrum grafu 1
# centrum minimax 1