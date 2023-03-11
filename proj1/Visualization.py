import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from DataTypes import AdjacencyList, AdjacencyMatrix, IncidenceMatrix, GraphData, FormatType
def draw_graph(graph: GraphData, filename: str = None) -> None:
    if graph.t == FormatType.AdjacencyList or graph.t == FormatType.IncidenceMatrix:
        graph = graph.to_adjacency_matrix()
    graph = nx.from_numpy_array(np.array(graph.data))
    nx.draw_circular(graph)
    if filename:
        plt.savefig(filename)
    else:
        plt.show()