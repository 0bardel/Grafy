from Global.GraphicSequence import graphFromSequence
from Global.RandomGraphs import randomize_graph
import networkx
import igraph


def main():
    n = 10
    k = 9
    random_count = 100

    if k >= n or (k%2==1 and n%2==1):
        raise Exception("Incorrect input values")

    sequence = [k] * n
    print(sequence)
    graph = graphFromSequence(sequence)
    #print(graph.get_adjacency())

    for _ in range(random_count):
        graph = randomize_graph(graph)
        
    print(igraph.Graph.from_networkx(graph).get_adjacency())
    
if __name__ == "__main__":
    main()