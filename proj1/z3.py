from DataTypes import *
from RandomGraphs import *

if __name__ == "__main__":

    graph = random_graph_by_edges(10, 12)

    print(graph)

    graph2 = random_graph_by_chance(10, 0.5)

    print(graph2)
