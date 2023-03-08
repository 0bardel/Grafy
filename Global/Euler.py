from typing import List
from igraph import Graph
import random
import numpy as np


def isSequenceGraphic(seq: List[int]) -> bool:

    seq = sorted(seq, reverse=True)

    while any(seq):
        first = seq[0]

        if first > len(seq) or any([val < 0 for val in seq]):
            return False

        for i in range(1, first):
            seq[i] -= 1
        seq[0] = 0

        seq = sorted(seq, reverse=True)

    else:
        return True
