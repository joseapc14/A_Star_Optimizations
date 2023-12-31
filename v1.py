import utilities as ut


def vw_a_star_1(graph, start, goal):
    frontier = ut.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    maze_size = len(graph.nodes)
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            temp = len(came_from) / maze_size
            if (
                next not in cost_so_far
                or new_cost < cost_so_far[next]
            ):
                cost_so_far[next] = new_cost
                w = 1 - temp  # changed
                priority = (
                    new_cost
                    + w * ut.heuristic(next, goal)
                )
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
