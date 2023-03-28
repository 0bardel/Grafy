from .DataTypes import *
import random


def generate_complete_edge_list(size: int) -> list[tuple[int, int]]:
    """Generates list of tuples representing all possible edges of a simple graph.
    No loops are generated.

    Args:
        size (int): Number of vertices.

    Returns:
        list[tuple[int, int]]: List of possible edges.
    """
    return list(
        [(x, y) for x in range(size) for y in range(size) if x < y]
    )  # I'm sorry.


def random_graph_by_edges(size: int, edges: int) -> AdjacencyList:
    """Generates random undirected graph with specific number of edges.

    Args:
        size (int): Number of vertices.
        edges (int): Number of edges.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    data = [[] for _ in range(size)]  # Initialize empty Adjacency List

    for n1, n2 in sorted(random.sample(generate_complete_edge_list(size), edges)):
        data[n1].append(n2)
        data[n2].append(n1)

    return AdjacencyList(size, data, edges)


def random_graph_by_chance(size: int, probability: float) -> AdjacencyList:
    """Generates random undirected graph with specified probability for any edge to appear.

    Args:
        size (int): Number of vertices.
        probability (float): Probability for an edge to be created.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    data = [[] for _ in range(size)]  # Initialize empty Adjacency List
    edges = 0

    for n1, n2 in generate_complete_edge_list(size):
        if random.random() <= probability:
            edges += 1
            data[n1].append(n2)
            data[n2].append(n1)

    return AdjacencyList(size, data, edges)


