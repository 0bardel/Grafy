from DataTypes import *
import random


def generateCompleteEdgeList(size: int) -> list[tuple[int, int]]:
    """Generates list of tuples representing all possible edges of a simple graph. No loops are generated.

    Args:
        size (int): Number of vertices.

    Returns:
        list[tuple[int, int]]: List of possible edges.
    """
    return list([(x, y) for x in range(size) for y in range(size) if x < y])


def randomGraphByEdges(size: int, edges: int) -> GraphData:
    """Generates random undirected graph with specific number of edges.

    Args:
        size (int): Number of vertices.
        edges (int): Number of edges.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    data = [[] for _ in range(size)]  # Initialize empty Adjancency List

    for n1, n2 in random.sample(generateCompleteEdgeList(size), edges):
        data[n1].append(n2)
        data[n2].append(n1)

    return GraphData(size, data, FormatType.AdjacencyList, edges)


def randomGraphByChance(size: int, probability: float) -> GraphData:
    """Generates random undirected graph with specific number of edges.

    Args:
        size (int): Number of vertices.
        probability (float): Probability for an edge to be created.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    data = [[] for _ in range(size)]  # Initialize empty Adjancency List
    edges = 0

    for n1, n2 in generateCompleteEdgeList(size):
        if random.random() < probability:
            edges += 1
            data[n1].append(n2)
            data[n2].append(n1)

    return GraphData(size, data, FormatType.AdjacencyList, edges)
