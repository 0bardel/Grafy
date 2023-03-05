from typing import Union
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


class AdjacencyMatrix(GraphData):
    pass
class AdjacencyList(GraphData):
    pass
class IncidenceMatrix(GraphData):
    pass


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

    def to_adjacency_matrix(self) -> AdjacencyMatrix:
        new_data = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for n1, row in enumerate(self.data):
            for n2 in row:
                new_data[n1][n2] = 1
        return AdjacencyMatrix(self.size, new_data, self.edges)

    def to_incidence_matrix(self) -> IncidenceMatrix:
        new_data = [[] for _ in range(self.size)]
        for n1, neighbors in enumerate(self.data):
            for n2 in neighbors:
                if n1 < n2:
                    for id, row in enumerate(new_data):
                        row.append(1 if id in (n1, n2) else 0)
        return IncidenceMatrix(self.size, new_data, self.edges)


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

    def to_adjacency_list(self) -> AdjacencyList:
        new_data = [[] for _ in range(self.size)]  # Initialize empty Adjacency List
        for n1, row in enumerate(self.data):
            for n2, value in enumerate(row):
                if value:
                    new_data[n1].append(n2)
        return AdjacencyList(self.size, new_data, self.edges)

    def to_incidence_matrix(self) -> IncidenceMatrix:
        new_data = [[0 for _ in range(self.edges)] for _ in range(self.size)]
        edges = 0
        for n1, row in enumerate(self.data):
            for n2, val in enumerate(row):
                if n1 > n2 and val:
                    new_data[n1][edges] = 1
                    new_data[n2][edges] = 1
                    edges += 1
        if edges != self.edges:
            raise ValueError("Coś się zepsuło")
        return IncidenceMatrix(self.size, new_data, self.edges)


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

    def to_adjacency_matrix(self) -> AdjacencyMatrix:
        new_data = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for edge in zip(*self.data):
            nodes = []
            for n, val in enumerate(edge):
                if val:
                    nodes.append(n)
            new_data[nodes[0]][nodes[1]] = 1
            new_data[nodes[1]][nodes[0]] = 1
        return AdjacencyMatrix(self.size, new_data, self.edges)

    def to_adjacency_list(self) -> AdjacencyList:
        new_data = [[] for _ in range(self.size)]
        for edge in zip(*self.data):
            nodes = []
            for n, val in enumerate(edge):
                if val:
                    nodes.append(n)
            new_data[nodes[0]].append(nodes[1])
            new_data[nodes[1]].append(nodes[0])
        return AdjacencyList(self.size, new_data, self.edges)
