from .DataTypes import *
from .RandomGraphs import *

if __name__ == "__main__":

    graph = random_graph_by_edges(11, 54)

    print(graph)

    graph2 = random_graph_by_chance(11, 1)

    print(graph2)
