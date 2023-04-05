import igraph as ig
import Global.RandomGraphs as rg
from matplotlib import pyplot as plt
import networkx as nx


def draw_graph(graph: ig.Graph):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True)


def components(graph):
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
    return max(all_comps, key=len)


def isHamilton(graph):
    comp = components(graph)
    if len(comp) == graph.__len__():
        return True
    else:
        return False


if __name__ == "__main__":
    graph = rg.randomGraphByEdges(5, 4).to_networkx()
    draw_graph(graph)
    plt.savefig("z6.png")
    plt.clf()
    print(isHamilton(graph))
