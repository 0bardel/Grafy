from typing import Union
import igraph
from enum import Enum, auto


class FormatType(Enum):
    Invalid = auto()
    AdjacencyList = auto()
    AdjacencyMatrix = auto()
    IncidenceMatrix = auto()


class GraphData:
    size: int
    data: list[list[int]]
    edges: Union[int, None]

    def __init__(
        self,
        size: int,
        data: list[list[int]],
        edges: int,
    ):
        self.data = data
        self.size = size
        self.edges = edges

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)


class AdjacencyList(GraphData):
    t: FormatType = FormatType.AdjacencyList

    def __init__(
        self,
        size: int,
        data: list[list[int]],
        edges: int,
    ):
        super().__init__(size, data, edges)

    def __str__(self):
        res = f"N: {self.size} L: {self.edges}\n"
        for index, neighbors in enumerate(self.data):
            res += f"{index}: {neighbors}\n"
        return res


class AdjacencyMatrix(GraphData):
    t: FormatType = FormatType.AdjacencyMatrix

    def __init__(
        self,
        size: int,
        data: list[list[int]],
        edges: int,
    ):
        super().__init__(size, data, edges)

    def __str__(self):
        res = f"N: {self.size} L: {self.edges}\n"
        for neighbors in self.data:
            res += f"{neighbors}\n"
        return res


class IncidenceMatrix(GraphData):
    t: FormatType = FormatType.IncidenceMatrix

    def __init__(
        self,
        size: int,
        data: list[list[int]],
        edges: int,
    ):
        super().__init__(size, data, edges)

    def __str__(self):
        res = f"N: {self.size} L: {self.edges}\n"
        for neighbors in self.data:
            res += f"{neighbors}\n"
        return res


# TODO: Refactor names, maybe reorganize.


def AL_to_AM(al: AdjacencyList) -> AdjacencyMatrix:
    newData = [[0 for _ in range(al.size)] for _ in range(al.size)]
    for n1, row in enumerate(al.data):
        for n2 in row:
            newData[n1][n2] = 1
    return AdjacencyMatrix(al.size, newData, al.edges)


def AM_to_AL(am: AdjacencyMatrix) -> AdjacencyList:
    newData = [[] for _ in range(am.size)]  # Initialize empty Adjancency List
    for n1, row in enumerate(am.data):
        for n2, value in enumerate(row):
            if value:
                newData[n1].append(n2)
    return AdjacencyList(am.size, newData, am.edges)


def AM_to_IM(am: AdjacencyMatrix) -> IncidenceMatrix:
    newData = [[0 for _ in range(am.edges)] for _ in range(am.size)]
    edges = 0
    for n1, row in enumerate(am.data):
        for n2, val in enumerate(row):
            if n1 > n2 and val:
                newData[n1][edges] = 1
                newData[n2][edges] = 1
                edges += 1
    if edges != am.edges:
        raise ValueError("Coś się zepsuło")
    return IncidenceMatrix(am.size, newData, am.edges)


def IM_to_AM(im: IncidenceMatrix) -> AdjacencyMatrix:
    newData = [[0 for _ in range(im.size)] for _ in range(im.size)]
    for edge in zip(*im.data):
        nodes = []
        for n, val in enumerate(edge):
            if val:
                nodes.append(n)
        newData[nodes[0]][nodes[1]] = 1
        newData[nodes[1]][nodes[0]] = 1

    return AdjacencyMatrix(im.size, newData, im.edges)


def IM_to_AL(im: IncidenceMatrix) -> AdjacencyList:
    newData = [[] for _ in range(im.size)]
    for edge in zip(*im.data):
        nodes = []
        for n, val in enumerate(edge):
            if val:
                nodes.append(n)
        newData[nodes[0]].append(nodes[1])
        newData[nodes[1]].append(nodes[0])

    return AdjacencyList(im.size, newData, im.edges)


def AL_to_IM(al: AdjacencyList) -> IncidenceMatrix:
    newData = [[] for _ in range(al.size)]
    for n1, neighbors in enumerate(al.data):
        for n2 in neighbors:
            if n1 < n2:
                for id, row in enumerate(newData):
                    row.append(1 if id in (n1, n2) else 0)

    return AdjacencyList(al.size, newData, al.edges)
