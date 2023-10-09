import heapq
import math
from typing import TypeVar

T = TypeVar("T")


class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, T]] = []
        self.size = 0

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(
            self.elements, (priority, item)
        )
        self.size += 1

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

    def get_size(self) -> int:
        return self.size


def heuristic(next, goal) -> float:
    (x1, y1) = next
    (x2, y2) = goal
    return math.sqrt(
        abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
    )


def get_path(d: dict, end):
    current = end
    path = [end]
    while d[current] != None:
        path.append(d[current])
        current = d[current]
    path.reverse()
    return path
