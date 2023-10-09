import math
import random
import utilities as ut


def vw_a_star_3(graph, start, goal):
    frontier = ut.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    temp = 1
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if (
                next not in cost_so_far
                or new_cost < cost_so_far[next]
            ):
                cost_so_far[next] = new_cost
                w = 1 / (       
                    math.exp(temp)
                    * random.random()
                )
                priority = (
                    new_cost
                    + w * ut.heuristic(next, goal)
                )
                frontier.put(next, priority)
                came_from[next] = current
    temp += 1

    return came_from, cost_so_far
