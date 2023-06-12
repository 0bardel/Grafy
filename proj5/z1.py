from proj4.z1 import DiGraph, draw_graph

import random as rd
import copy


def generate_flow_newtwork(N, verbose=False):
    shape = [rd.randint(2, N) for _ in range(N)]
    tracker = 0
    for i, n in enumerate(shape):
        shape[i] = list(range(tracker, tracker+n))
        tracker += n
    if verbose:
        print(shape)
    G = DiGraph(0)
    G.add_vertex(len(shape[0]))
    for i in range(1, len(shape)):
        G.add_vertex(len(shape[i]))
        v_from = copy.deepcopy(shape[i-1])
        v_to = copy.deepcopy(shape[i])
        rd.shuffle(v_from)
        rd.shuffle(v_to)
        edge_number = max(len(v_from), len(v_to))
        for j in range(edge_number):
            # print(v_from[j % len(v_from)], v_to[j % len(v_to)])
            G.add_random_weighted_edge(
                v_from[j % len(v_from)], v_to[j % len(v_to)], 1, 10, can_Self=False)
    for _ in range(2*N):
        # print(G.edges)
        G.add_random_edge(weight_range=(1, 10),
                          is_weighted=True, can_Self=False)
    G.add_vertex()
    for v in shape[0]:
        G.add_random_weighted_edge(G.n-1, v, 1, 10)
    G.add_vertex()
    for v in shape[-1]:
        G.add_random_weighted_edge(v, G.n-1, 1, 10)
    return G


if __name__ == '__main__':
    G = generate_flow_newtwork(3, True)
    draw_graph(G, 'flow_network.png')
