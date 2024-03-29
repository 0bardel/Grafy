import igraph as ig
import Global.RandomGraphs as rg
from matplotlib import pyplot as plt
import networkx as nx


def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


def components(graph, show_all=False):  
    def components_rec(graph, node, visited, comp):
        visited.add(node)
        comp.append(node)
        for u in graph.neighbors(node):
            if u not in visited:
                components_rec(graph, u, visited, comp)

    visited = set()
    all_comps = []
    for node in graph.nodes():
        if node not in visited:
            comp = []
            components_rec(graph, node, visited, comp)
            all_comps.append(comp)
    if show_all:
        return all_comps
    return max(all_comps, key=len)

if __name__ == "__main__":

    graph = rg.randomGraphByEdges(13, 12).to_networkx()
    draw_graph(graph)
    plt.savefig("z3.png")
    plt.clf()
    comp = components(graph, False)
    print(comp)

