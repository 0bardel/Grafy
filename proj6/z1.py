import numpy as np
import random
import math

def page_rank_random(digraph: dict, d=0.15, max_iterations=1000):
    n = len(digraph)
    vertices = [0 for _ in range(n)]
    vertex = 0

    for _ in range(max_iterations):
        option = random.uniform(0, 1)
        if option < d:
            vertex = random.choice(range(n))
        else:
            vertex = random.choice(digraph[vertex])
        vertices[vertex] += 1
        
    vertices = [p/max_iterations for p in vertices]
    return vertices


def page_rank_iter(digraph, d=0.15, max_iterations=1000, convergence_threshold=0.0001):
    n = len(digraph)

    # stworzenie macierzy sąsiedztwa z prawdopodobieństwem wyjścia z wierzchołka
    adjacency_matrix_probability = np.zeros((n, n))
    for node, neighbors in digraph.items():
        if neighbors:
            for neighbor in neighbors:
                adjacency_matrix_probability[neighbor][node] = 1 / len(neighbors)

    pagerank_vector = np.full(n, 1 / n)
    teleportation_vector = np.full(n, 1 / n)

    for _ in range(max_iterations):
        prev_pagerank_vector = pagerank_vector.copy()

        for node in range(n):
            pagerank_vector[node] = (1 - d) * np.dot(adjacency_matrix_probability[node], prev_pagerank_vector) + d * np.dot(teleportation_vector, prev_pagerank_vector)

        if math.sqrt(np.sum(np.square(pagerank_vector - prev_pagerank_vector))) < convergence_threshold:
            break

    return pagerank_vector

# Przykładowe dane wejściowe w postaci listy sąsiedztwa
digraph_input = {
    0: [4, 5, 8],
    1: [0, 2, 5],
    2: [1, 3, 4, 11],
    3: [2, 4, 7, 8, 10],
    4: [2, 6, 7, 8],
    5: [2, 6],
    6: [4, 5, 7],
    7: [3, 6, 8, 11],
    8: [3, 4, 7, 9],
    9: [8],
    10: [3, 8],
    11: [0, 7]
}

digraph_presentation = {
    0: [1, 3, 4],
    1: [2, 4],
    2: [1, 3, 5],
    3: [1],
    4: [1, 3, 5],
    5: [1],
}
# a - 0
# b - 1
# c - 2
# d - 3
# e - 4
# f - 5
# g - 6

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

# Wywołanie funkcji pagerank
# page_rank = pagrank(digraph, d=0.15, max_iterations=1000000)
page_rank = page_rank_random(digraph=digraph_input, max_iterations=1000000)

# Sortowanie stron internetowych według wartości PageRank
sorted_pages = sorted(range(len(page_rank)), key=lambda k: page_rank[k], reverse=True)

# Wyświetlenie rankingów stron internetowych wraz z wartościami PageRank
for rank, page in enumerate(sorted_pages):
    print(f"Rank {rank+1}: Page {alfabet[page]}, PageRank: {page_rank[page]}")

print("------")

# Wywołanie funkcji pagerank
# page_rank = pagrank(digraph, d=0.15, max_iterations=1000000)
page_rank = page_rank_iter(digraph=digraph_input, max_iterations=1000000)

# Sortowanie stron internetowych według wartości PageRank
sorted_pages = sorted(range(len(page_rank)), key=lambda k: page_rank[k], reverse=True)

# Wyświetlenie rankingów stron internetowych wraz z wartościami PageRank
for rank, page in enumerate(sorted_pages):
    print(f"Rank {rank+1}: Page {alfabet[page]}, PageRank: {page_rank[page]}")