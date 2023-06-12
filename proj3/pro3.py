import proj1.DataTypes
import proj1.RandomGraphs as rg
import proj2.z3 as cmp
import random
import networkx
import numpy as np
import copy

def random_graph_weights(size: int, edges:int, min_weight : int =1, max_weight : int =10 ):
    
    # step 1: generate random graph without weights
    components_count = 0
    while(components_count != 1):
        graph = rg.random_graph_by_edges(size,edges).to_adjacency_matrix()
        nx = networkx.Graph(np.array(graph.data))
        components_count = len(cmp.components(nx,True)) 
    
    
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
    
def dijkstra(graph, start: int = 0, verbose: bool = True):

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
    if not verbose:
        return d
        
    for vertex in range(graph.size):
        res = ''
        distance = d[vertex]
        while p[vertex] is not None:
            res = ' -> ' + str(vertex) + res
            vertex = p[vertex]
            
        res = str(start) + res
        print(distance, res)
    
    
def find_min(data,start,end):
    min_len = None
    
    for s in start:
        for e in end:
            if (not (data[s][e] is None)) and (min_len is None or data[s][e] < min_len):
                min_len = data[s][e]
                min_ind = (s,e)

    return min_ind

def prim(graph):
    tree = [0]
    rest = list(range(1,graph.size))
    
    result = copy.deepcopy(graph.data)
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = None
        
    while(len(tree) < graph.size):
        i,j = find_min(graph.data,tree,rest)
        result[i][j] = graph.data[i][j]
        result[j][i] = graph.data[i][j]
        rest.remove(j)
        tree.append(j)
        
    return result