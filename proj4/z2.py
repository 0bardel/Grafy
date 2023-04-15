try:
    from proj4.z1 import *
except:
    from z1 import *

def dfs_visit(G, v, d, f, t):
    t += 1
    d[v] = t

    for u, _ in G.adj[v]:
        if d[u] == -1:
            t = dfs_visit(G, u, d, f, t)
    t += 1
    f[v] = t
    return t 


def components_rec(G, v, comp, nr):
    for u, _ in G.adj[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_rec(G, u, comp, nr)


def kosaraju(G,verbose=False):
    d = [-1 for _ in range(G.n)]
    f = [-1 for _ in range(G.n)]

    t = 0

    # [dfs_visit(G, v, d, f, t) for v in range(G.n) if d[v] == -1]
    for v in range(G.n):
        if d[v] == -1:
            t = dfs_visit(G, v, d, f, t)

    if verbose:
        print("d: ", d)
        print("f: ", f)

    Gt = G.get_transpose()

    nr = 0
    comp = [-1 for _ in range(Gt.n)]

    for v in sorted(list(range(Gt.n)), key=lambda v: f[v], reverse=True):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_rec(Gt, v, comp, nr)

    return comp

# generate main 
if __name__ == "__main__":
    # sample from presentation
    G = DiGraph(7).add_edge(1, 0).add_edge(0, 6).add_edge(6, 0).add_edge(1, 5).add_edge(1, 2).add_edge(2, 1).add_edge(5, 4).add_edge(4,2).add_edge(2, 5).add_edge(3, 2).add_edge(3, 4).add_edge(1, 6)
    draw_graph(G,'z2.png')
    print(G.get_adj_matrix())
    print(kosaraju(G, verbose=True))

    # random sample
    G = generate_rand_graph(5, 0.25)
    draw_graph(G,'z2_rand.png')
    print(G.get_adj_matrix())
    print(kosaraju(G, verbose=True))


