from igraph import Graph
import random


def generateCompleteEdgeList(size: int) -> list[tuple[int, int]]:
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


def randomGraphByEdges(size: int, edges: int) -> Graph:
    """Generates random undirected graph with specific number of edges.

    Args:
        size (int): Number of vertices.
        edges (int): Number of edges.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    return Graph(size, random.sample(generateCompleteEdgeList(size), edges))


def randomGraphByChance(size: int, probability: float) -> Graph:
    """Generates random undirected graph with specified probability for any edge to appear.

    Args:
        size (int): Number of vertices.
        probability (float): Probability for an edge to be created.

    Returns:
        GraphData: Object in AdjacencyList format.
    """
    edgeList = list(
        [e for e in generateCompleteEdgeList(size) if random.random() <= probability]
    )
    return Graph(size, edgeList)
