import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class DiGraph:
    def __init__(self, n):
        self.n = n
        self.edges = []
        self.adj = [[] for _ in range(n)]
        self.in_deg = [0 for _ in range(n)]
        self.out_deg = [0 for _ in range(n)]

    def add_edge(self, u, v, w=1, can_Parallel=True, can_Self=True):
        if u == v and not can_Self:
            raise ValueError("Self loops are not allowed")

        check = [(u, v) for u, v, _ in self.edges]
        if ((u, v) in check or (v, u) in check) and not can_Parallel:
            raise ValueError("Parallel edges are not allowed")

        self.edges.append((u, v, w))
        self.adj[u].append((v, w))
        self.in_deg[v] += 1
        self.out_deg[u] += 1
        return self

    def add_random_weighted_edge(self, u, v, min=1, max=10, can_Parallel=True, can_Self=True):
        w = random.randint(min, max)
        return self.add_edge(u, v, w, can_Parallel, can_Self)

    def add_random_edge(self, weight_range=(1, 10), is_weighted=False, can_Self=True, can_Parallel=True):
        u = random.randint(0, self.n - 1)
        v = random.randint(0, self.n - 1)
        w = random.randint(*weight_range)

        try:
            return self.add_edge(u, v, w if is_weighted else 1, can_Parallel, can_Self)
        except ValueError:
            return self.add_random_edge(weight_range, is_weighted, can_Self, can_Parallel)

    def get_adj_matrix(self):
        matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for u, v, w in self.edges:
            matrix[u][v] = w
        return np.array(matrix)

    def get_transpose(self):
        Gt = DiGraph(self.n)
        for u, v, w in self.edges:
            Gt.add_edge(v, u, w)
        return Gt

    def add_vertex(self, n=1):
        self.n += n
        self.adj.extend([[] for _ in range(n)])
        self.in_deg.extend([0 for _ in range(n)])
        self.out_deg.extend([0 for _ in range(n)])
        return self

    def __str__(self):
        return str(self.edges)


def generate_rand_graph(n, p, weight_range=None, seed=None):
    if seed is not None:
        random.seed(seed)
    G = DiGraph(n)
    for u in range(n):
        for v in range(n):
            if u != v and random.random() < p:
                try:
                    if weight_range is None:
                        G.add_edge(u, v)
                    else:
                        G.add_random_weighted_edge(u, v, *weight_range)
                except ValueError:
                    pass
    return G


def draw_graph(g, filename):
    # Create an instance of the DiGraph class
    plt.figure()
    G = nx.DiGraph(g.get_adj_matrix())

    # Define the positions of the nodes
    pos = nx.circular_layout(G)

    # Draw the graph
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(
        u, v): d['weight'] for u, v, d in G.edges(data=True)})
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->')

    # Show the plot
    plt.savefig(filename)


# crate main and test Graph
if __name__ == "__main__":
    g = DiGraph(5).add_random_edge(is_weighted=True).add_random_edge(is_weighted=True).add_random_edge(
        is_weighted=True).add_random_edge(is_weighted=True).add_random_edge(is_weighted=True).add_random_edge(is_weighted=True)

    print(g.edges)
    draw_graph(g, "graph.png")
