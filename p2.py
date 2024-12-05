import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def astar(start):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        _, state, path = heapq.heappop(queue)
        if state == GOAL:
            return path + [state]

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        for i, x in enumerate(state):
            if x == 0:
                continue
            for dx, dy in [(-3, 0), (3, 0), (-1, 0), (1, 0)]:
                ni = i + dx
                if 0 <= ni < 9:
                    neighbor = list(state)
                    neighbor[i], neighbor[ni] = neighbor[ni], neighbor[i]
                    heapq.heappush(queue, (len(path) + 1 + abs(ni % 3 - GOAL.index(0) % 3) + abs(ni // 3 - GOAL.index(0) // 3), neighbor, path + [state]))

start = (5, 2, 0, 4, 1, 8, 7, 3, 6)
print(astar(start))
