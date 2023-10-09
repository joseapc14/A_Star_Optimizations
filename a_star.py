import utilities as ut


def a_star_search(graph, start, goal):
    frontier = ut.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

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
                priority = (
                    new_cost
                    + ut.heuristic(next, goal)
                )
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
