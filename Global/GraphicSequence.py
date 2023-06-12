from typing import List, Union
from igraph import Graph
import random
import numpy as np


def isSequenceGraphic(seq: List[int]) -> bool:
    """Asserts whether given sequence is graphic.

    Args:
        seq (List[int]): Tested sequence. The list is passed by reference and WILL get modified

    Returns:
        bool: Assertion result
    """

    seq.sort(reverse=True)

    while any(seq):
        first = seq[0]

        if first >= len(seq) or any((val < 0) for val in seq):
            return False

        for i in range(1, first+1):
            seq[i] -= 1
        seq[0] = 0

        seq.sort(reverse=True)

    else:
        return True


def graphFromSequence(seq: List[int]) -> Graph:
    """Builds a graph from provided graphic sequence.

    Args:
        seq (List[int]): Provided sequence.

    Returns:
        Graph: Built igraph object.
    """
    if not isSequenceGraphic(seq.copy()):
        raise ValueError("Non-graphic sequence was given.")

    vertexList = [
        [i, deg] for i, deg in enumerate(seq)
    ]  # list of modifiable index-degree pairs
    edgeList = []

    vertexList.sort(key=lambda x: x[1], reverse=True)

    while any(v[1] for v in vertexList):
        first = vertexList[0]

        for i in range(0, first[1]):
            vertexList[i + 1][1] -= 1
            edgeList.append((first[0], vertexList[i + 1][0]))

        first[1] = 0

        vertexList.sort(key=lambda x: x[1], reverse=True)
    return Graph(len(seq), edgeList)
