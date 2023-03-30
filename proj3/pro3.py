import proj1.DataTypes
import proj1.RandomGraphs as rg
import random

# TODO: SPRAWDZ CZY GRAF JEST SPOJNY
def random_graph_weights(size: int, edges:int, min_weight : int =1, max_weight : int =10 ):
    
    # step 1: generate random graph without weights
    graph = rg.random_graph_by_edges(size,edges).to_adjacency_matrix()
    
    # step 2: assign random weights to edges
    for i in range(len(graph.data)):
        for j, val in enumerate(graph.data[i]):
            if j > i:
                continue
            if val != 0:
                curr = random.randint(min_weight,max_weight)
                graph.data[i][j] = curr
                graph.data[j][i] = curr
            else:
                graph.data[i][j] = None
                graph.data[j][i] = None                   
                
    return graph
    
def dijkstra(graph, start: int = 0):

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
        
        # realax
        for v in [vertex for vertex in range(graph.size) if (vertex not in ready and graph.data[u][vertex] is not None)]:
            if d[v] > d[u] + graph.data[u][v]:
                d[v] = d[u] + graph.data[u][v]
                p[v] = u


    # print results
    for vertex in range(graph.size):
        res = ''
        distance = d[vertex]
        while p[vertex] is not None:
            res = ' -> ' + str(vertex) + res
            vertex = p[vertex]
            
        res = str(start) + res
        print(distance, res)
    