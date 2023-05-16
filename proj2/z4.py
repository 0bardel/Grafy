from Global.GraphicSequence import isSequenceGraphic, graphFromSequence
from proj2.z3 import components
import random
import numpy as np
import networkx

n = random.randint(5,6)

sequence = [0,2]
while (not isSequenceGraphic(sequence.copy())) or len(components(graphFromSequence(sequence).to_networkx(),True)) != 1 :
    sequence = [random.randint(1,(n-1)//2)*2 for _ in range(n)]

print(sequence)
graph = graphFromSequence(sequence)
graph = np.array(graph.get_adjacency().data)
print(graph)


euler = [0]
while np.sum(graph)>0:
    curr = euler[-1]
    for i,option in enumerate(graph[curr]):
        if option != 0:
            test_graph = graph.copy()
            test_graph[i][curr] = 0
            test_graph[curr][i] = 0
            if (len([x for x in components(networkx.Graph(test_graph),True) if len(x)>1]) == 1 and np.sum(test_graph[i])>0) or np.sum(test_graph)<1e-6:
                euler.append(i)
                graph[i][curr] = 0
                graph[curr][i] = 0
                break
                
print(euler)
