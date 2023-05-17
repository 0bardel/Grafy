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


# N: 8 L: 12
# [None, 10, None, 10, None, 6, None, 4]
# [10, None, None, None, 5, 2, None, None]
# [None, None, None, None, None, None, 5, None]
# [10, None, None, None, None, None, 3, 3]
# [None, 5, None, None, None, None, 9, None]
# [6, 2, None, None, None, None, None, 8]
# [None, None, 5, 3, 9, None, None, 6]
# [4, None, None, 3, None, 8, 6, None]

# [[ 0.  8. 15.  7. 13.  6. 10.  4.]
#  [ 8.  0. 19. 13.  5.  2. 14. 10.]
#  [15. 19.  0.  8. 14. 19.  5. 11.]
#  [ 7. 13.  8.  0. 12. 11.  3.  3.]
#  [13.  5. 14. 12.  0.  7.  9. 15.]
#  [ 6.  2. 19. 11.  7.  0. 14.  8.]
#  [10. 14.  5.  3.  9. 14.  0.  6.]
#  [ 4. 10. 11.  3. 15.  8.  6.  0.]]