import matplotlib.pyplot as plt
import networkx as nx
import random as random
import heapq
import math
from typing import TypeVar
import time


T = TypeVar("T")


def create_maze(given_cols):
    num_cols = given_cols
    num_rows = int(num_cols / 2)
    start = (0, 0)
    end = (num_cols - 1, num_rows - 1)
    G = nx.Graph()
    for i in range(num_cols):
        for j in range(num_rows):
            G.add_node((i, j))

    create_edges(G, num_cols)

    return [G, start, end]


def get_valid_negihbors(pair, columns):
    y, x = pair
    neighbors = []
    if y != 0:
        neighbors.append((y - 1, x))
    if x != 0:
        neighbors.append((y, x - 1))
    if y != columns - 1:
        neighbors.append((y + 1, x))
    if x != int(columns / 2) - 1:
        neighbors.append((y, x + 1))
    return neighbors


def create_edges(G, cols):
    possible_neighbors = {}
    for node in G.nodes():
        possible_neighbors[
            node
        ] = get_valid_negihbors(node, cols)

    stack = [(0, 0)]
    visited = {(0, 0)}
    while len(stack) > 0:
        current = stack.pop()
        if len(possible_neighbors[current]) != 0:
            options = []
            for neighbor in possible_neighbors[
                current
            ]:
                if neighbor not in visited:
                    options.append(neighbor)
            if len(options) != 0:
                stack.append(current)
                selected = random.choice(options)
                G.add_edge(current, selected)
                stack.append(selected)
                visited.add(selected)


def draw_maze(G, start, end, path):
    background = plt.axes()
    background.set_facecolor("black")
    labels = {start: "■", end: "■"}

    pos = {}
    for node in list(nx.nodes(G)):
        pos[node] = node

    nx.draw_networkx_labels(
        G,
        pos,
        labels,
        font_size=15,
        font_color="green",
    )

    nx.draw(
        G,
        node_color="purple",
        node_size=150,
        edge_color="purple",
        node_shape="s",
        width=10,
        pos=pos,
    )
    nx.draw_networkx_nodes(
        G,
        pos=pos,
        nodelist=path,
        node_size=60,
        node_color="green",
        node_shape="s",
        edgecolors="green",
    )

    ax = plt.gca()

    ax.set_aspect("equal", adjustable="box")
    plt.tight_layout()
    plt.show()
