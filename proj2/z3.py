import igraph as ig
import Global.RandomGraphs as rg
from matplotlib import pyplot as plt
import networkx as nx


def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


def components(graph):

    def components_rec(adj_list, comp, nr, v):
        for u in adj_list[v]:
            if comp[u][0] == -1:
                comp[u].append(nr)
                components_rec(adj_list, comp, nr, u)
        return comp

    adj_list = dict(graph.adjacency())
    comp = [[-1] for _ in range(len(adj_list))]
    nr = 0
    for v in range(len(comp)):
        if comp[v][0] == -1:
            comp[v].remove(-1)
            # comp[v].append(nr)
            comp = components_rec(adj_list, comp, nr, v)
            nr += 1
    return comp


if __name__ == "__main__":

    graph = rg.randomGraphByEdges(10, 5).to_networkx()
    draw_graph(graph)
    plt.savefig("z3.png")
    plt.clf()
    comp = components(graph)
    print(comp)
    adj_list = dict(graph.adjacency())
    for node, neighbours in adj_list.items():
        print(node, ':', list(neighbours))