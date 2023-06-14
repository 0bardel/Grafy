from proj5.z1 import generate_flow_newtwork
from proj4.z1 import DiGraph, draw_graph


def bfs(graph: DiGraph, s: int, t: int):
    d = [float("inf") for _ in range(graph.n)]
    p = [None for _ in range(graph.n)]
    d[s] = 0
    visited = [False for _ in range(graph.n)]
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
        last_v = queue.pop(0)
        if last_v == t:
            break
        for v, w in graph.adj[last_v]:
            if not visited[v] and w > 0:
                queue.append(v)
                visited[v] = True
                d[v] = d[last_v] + w
                p[v] = last_v
    return d, p


def find_extending_path(graph: DiGraph, s: int, t: int):
    d, p = bfs(graph, s, t)
    if d[t] == float("inf"):
        return None
    path = []
    c = float("inf")
    v = t
    while v != s:
        edge = (p[v], v)
        c = min(c, graph.get_edge_value(*edge))
        path.append(edge)
        v = p[v]
    path.reverse()
    return path, c


def ford_fulkerson(graph: DiGraph, s: int, t: int):
    while True:
        result = find_extending_path(graph, s, t)
        if result is None:
            break
        path, c = result
        for edge in path:
            graph.add_edge_value(*edge, -c)
            graph.add_edge_value(edge[1], edge[0], c)
    return sum([w for _, w in graph.adj[t]])


if __name__ == '__main__':
    # random
    G = generate_flow_newtwork(2, True)
    draw_graph(G, 'fulkerson_random.png')
    print(G)
    print(ford_fulkerson(G, G.n-2, G.n-1))
    # z wykładu
    G = DiGraph(11)
    G.add_edge(0, 1, 10).add_edge(0, 2, 3).add_edge(0, 3, 6).add_edge(3, 6, 1).add_edge(3, 4, 9).add_edge(2, 5, 2).add_edge(1, 2, 8).add_edge(1, 4, 8).add_edge(1, 5, 6).add_edge(
        2, 6, 10).add_edge(4, 8, 5).add_edge(5, 4, 1).add_edge(5, 9, 7).add_edge(6, 7, 9).add_edge(8, 6, 8).add_edge(9, 10, 7).add_edge(8, 10, 5).add_edge(8, 7, 1).add_edge(7, 10, 7)
    draw_graph(G, 'fulkerson_lecture.png')
    print(G)
    print(ford_fulkerson(G, 0, 10))
