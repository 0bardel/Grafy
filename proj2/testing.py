import igraph as ig
from matplotlib import pyplot as plt
import Global.RandomGraphs as rg
import networkx as nx
from Global.GraphicSequence import isSequenceGraphic, graphFromSequence
from proj2.z3 import components
import random
import numpy as np
import networkx


def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


if __name__ == "__main__":

    graph = graphFromSequence([3, 3, 3, 3, 2, 2, 2]).to_networkx()
    draw_graph(graph)
    plt.savefig("test.png")
