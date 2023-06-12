from proj4.z1 import *
from proj4.z2 import *

def bellman_ford(G,s):
    d = [float("inf") for _ in range(G.n)]
    p = [None for _ in range(G.n)]
    d[s] = 0

    for _ in range(G.n-1):
        for u, v, w in G.edges:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u
    for u, v, w in G.edges:
        if d[v] > d[u] + w:
            return False
    return d, p



def coherentate(g):
    comp = kosaraju(g)
    while True:
        m = max(comp)
        if m == 1:
            break
        u = comp.index(m)
        v = comp.index(m-1)
        print(u, v)
        print(comp)
        try:
            g.add_random_weighted_edge(u, v)
        except:
            g.add_random_weighted_edge(v, u)
        
        while True:
            try:
                comp[comp.index(m)] -= 1
            except:
                break
    
    print(comp)
    return g

# generate main __name__
if __name__ == "__main__":
    g = generate_rand_graph(10, 0.23, (-5, 10))
    draw_graph(g, 'z3.png')
    coherentate(g)
    draw_graph(g, 'z3_weighted.png')
    # G = DiGraph(7).add_edge(1, 0).add_edge(0, 6).add_edge(6, 0).add_edge(1, 5).add_edge(1, 2).add_edge(2, 1).add_edge(5, 4).add_edge(4,2).add_edge(2, 5).add_edge(3, 2).add_edge(3, 4).add_edge(1, 6)
    G = DiGraph(7).add_edge(0,1,6).add_edge(1,0,10).add_edge(0,2,3).add_edge(0,4,-1).add_edge(1,4,4).add_edge(1,2,-5).add_edge(2,5,2).add_edge(5,1,9).add_edge(1,3,-4).add_edge(3,1,5).add_edge(1,6,4).add_edge(3,6,9).add_edge(4,6,-4).add_edge(6,5,4)
    # draw_graph(G, 'z3test.png')
    # G = generate_rand_graph(8, 0.23, (-5, 10))
    d, p = bellman_ford(G, 0)
    draw_graph(G, 'z3_bellmonto.png')
    # print(d)
    # print(p)
    g2 = DiGraph(3).add_edge(0,1,-1).add_edge(1,0,4).add_edge(0,2,-4).add_edge(2,1,2)
    d, p = bellman_ford(g2, 0)
    print(d)
    print(p)




