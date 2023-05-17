import igraph as ig
from matplotlib import pyplot as plt
import Global.RandomGraphs as rg
import networkx as nx
import Global.GraphicSequence


def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


if __name__ == "__main__":

    graph = Global.GraphicSequence.graphFromSequence([6,6,6,4,4,2,2,2]).to_networkx()
    draw_graph(graph)
    plt.savefig("z2.png")
    plt.clf()
    graph = rg.randomize_graph(graph)
    draw_graph(graph)
    plt.savefig("z2_2.png")


