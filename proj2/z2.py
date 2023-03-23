import igraph as ig
from matplotlib import pyplot as plt
import Global.RandomGraphs as rg
import networkx as nx

def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


if __name__ == "__main__":

    graph = rg.randomGraphByEdges(5, 5).to_networkx()
    draw_graph(graph)
    plt.savefig("z2.png")
    plt.clf()
    graph = rg.randomize_graph(graph)
    draw_graph(graph)
    plt.savefig("z2_2.png")



