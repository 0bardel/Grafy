import proj1.DataTypes
import proj1.RandomGraphs as rg
import random

def random_graph_weights(size: int, edges:int, min_weight : int =1, max_weight : int =10 ):
    
    # step 1: generate random graph without weights
    graph = rg.random_graph_by_edges(size,edges).to_adjacency_matrix()
    
    # step 2: assign random weights to edges
    for i in range(len(graph.data)):
        for j, val in enumerate(range(len(graph.data[i]))):
            if j < i and val != 0:
                curr = random.randint(min_weight,max_weight)
                graph.data[i][j] = curr
                graph.data[j][i] = curr
                
    return graph
    

