from proj4.z1 import *
from proj4.z2 import *
from proj4.z3 import *
import numpy as np


def dijkstra(G, s):
    d = [float("inf") for _ in range(G.n)]
    p = [None for _ in range(G.n)]
    d[s] = 0
    Q = set(range(G.n))
    while Q:
        u = min(Q, key=lambda x: d[x])
        Q.remove(u)
        for v, w in G.adj[u]:
            if not v in Q:
                continue
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u
    return d, p


def add_s(G):
    Gt = G.get_copy()
    Gt.add_vertex()
    for v in range(G.n):
        Gt.add_edge(Gt.n - 1, v, 0)
    return Gt


# johnson algorithm
def johnson(G):
    Gs = add_s(G)
    bf = bellman_ford(Gs, G.n - 1)
    if not bf:
        return None
    d, p = bf
    h = [i for i in d]
    for i, (u, v, w) in enumerate(Gs.edges):
        # print(f"{i=} {u=} {v=} {w=}")
        Gs.edges[i] = (u, v, w + h[u] - h[v])

    G2 = Gs.get_copy()
    print(G2)
    D = np.zeros((G.n, G.n))
    for u in range(G.n):
        d2, _ = dijkstra(G2, u)
        for v in range(G.n):
            D[u][v] = d2[v] - h[u] + h[v]
    return D


if __name__ == "__main__":
    # johnson
    # G = coherentate(generate_rand_graph(4, 0.23, (-5, 10)))
    G = (
        DiGraph(7)
        .add_edge(0, 1, 6)
        .add_edge(1, 0, 10)
        .add_edge(0, 2, 3)
        .add_edge(0, 4, -1)
        .add_edge(1, 4, 4)
        .add_edge(1, 2, -5)
        .add_edge(2, 5, 2)
        .add_edge(5, 1, 9)
        .add_edge(1, 3, -4)
        .add_edge(3, 1, 5)
        .add_edge(1, 6, 4)
        .add_edge(3, 6, 9)
        .add_edge(4, 6, -4)
        .add_edge(6, 5, 4)
        .add_edge(2, 5, 2)
    )
    print(G)
    draw_graph(G, "z4.png")
    D = johnson(G)
    print(D)
