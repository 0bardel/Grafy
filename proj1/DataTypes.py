from typing import Union
import igraph
from dataclasses import dataclass
from enum import Enum, auto


class FormatType(Enum):
    Invalid = auto()
    AdjacencyList = auto()
    AdjacencyMatrix = auto()
    IncidenceMatrix = auto()


class GraphData:
    size: int
    data: list[list[int]]
    type: FormatType
    edges: Union[int, None]

    def __init__(self):
        self.data = None
        self.size = 0
        self.type = FormatType.Invalid

    def __init__(
        self,
        size: int,
        data: list[list[int]],
        type: FormatType,
        edges: Union[int, None] = None,
    ):
        self.data = data
        self.size = size
        self.type = type
        self.edges = edges

    def __repr__(self):
        return self.data

    def __str__(self):
        return str(self.data)
