import proj3.pro3 as p3

# 1

graph = p3.random_graph_weights(8,12)
print(graph)

# 2
print(graph.data)
p3.dijkstra(graph)

# [[None, 2, None, 7, 6, None, 7, None], [2, None, 3, None, None, None, 5, None], [None, 3, None, 7, 7, None, None, None], [7, None, 7, None, None, None, 9, None], [6, None, 7, None, None, 2, 4, 8], [None, None, None, None, 2, None, None, None], [7, 5, None, 9, 4, None, None, None], [None, None, None, None, 8, None, None, None]]
# 0 0
# 2 0 -> 1
# 5 0 -> 1 -> 2
# 7 0 -> 3
# 6 0 -> 4
# 8 0 -> 4 -> 5
# 7 0 -> 6
# 14 0 -> 4 -> 7
