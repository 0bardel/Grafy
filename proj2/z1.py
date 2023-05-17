from igraph import Graph
import numpy as np
from Global.GraphicSequence import *
from Global.RandomGraphs import *
from matplotlib import pyplot as plt
import igraph as ig


def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


if __name__ == "__main__":
    sequence1 = [2]*7
    sequence2 = [6, 2, 5, 6, 1, 3]
    sequence3 = [4, 0, 0, 0, 0]

    print(f"{sequence1} -> {isSequenceGraphic(sequence1)}")
    print(f"{sequence2} -> {isSequenceGraphic(sequence2)}")
    print(f"{sequence3} -> {isSequenceGraphic(sequence3)}")

    graph = graphFromSequence([2,2,2,2,2,2,3])

    draw_graph(graph.to_networkx())
    plt.savefig("z1.png")
    plt.clf()

    print(graph.to_tuple_list())
    print(graph.get_adjlist())
