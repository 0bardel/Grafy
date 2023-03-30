import proj3.pro3 as p3

# 1

graph = p3.random_graph_weights(10,10)
print(graph)

# 2

start = 0

d = {}
p = {}


# initialisation
for vertex in range(graph.size):
    d[vertex] = float('inf')
    p[vertex] = None

d[start] = 0

ready = set()

while len(ready) < graph.size:
    
    # to na pewno da sie zrobic szybciej jezeli wydajnosc jest problemem
    u = sorted([vertex for vertex in range(graph.size) if vertex not in ready], key=d.get)[0]
    ready.add(u)
    for v in [vertex for vertex in range(graph.size) if (vertex not in ready and graph.data[vertex] != None)]:
        pass
