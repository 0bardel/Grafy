import igraph as ig
import Global.GraphicSequence
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

def walk(graph,cycle,current_node):
    if len(cycle) == len(graph[0]) and graph[current_node][cycle[0]]:
        return cycle
    
    for node,exists in enumerate(graph[current_node]):
        if exists and node not in cycle:
            cycle_copy = cycle.copy()
            cycle_copy.append(node)
            walk_res =  walk(graph,cycle_copy,node)
            if walk_res:
                return walk_res
            
    return False

def isHamilton(graph):
    comp = components(graph)
    if len(comp) == graph.__len__():
        start_node = 0
        cycle = [0]
        return walk(nx.to_numpy_array(graph),cycle,start_node)
    else:
        return False


if __name__ == "__main__":
    graph = Global.GraphicSequence.graphFromSequence([2,2,2,2,2,2]).to_networkx()
    for _ in range(10):
        graph = rg.randomize_graph(graph)
    draw_graph(graph)
    plt.savefig("z6.png") #save randomly generated graph
    plt.clf()
    print(isHamilton(graph))
