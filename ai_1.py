from collections import deque

# Goal state (0 = blank)
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Positions:   0 1 2
#              3 4 5
#              6 7 8
# For each blank position, which squares it can swap with
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


def bfs(start):
    queue = deque([(start, [])])   # to-do list: (state, path so far)
    visited = set([start])         # seen-it list

    while queue:
        state, path = queue.popleft()      # 1. POP from front

        if state == goal:                  # 2. GOAL?
            return path + [state]

        zero = state.index(0)              # 3. FIND blank

        for move in moves[zero]:
            new_state = list(state)        # L: tuple -> list
            new_state[zero], new_state[move] = new_state[move], new_state[zero]   # S: swap
            new_state = tuple(new_state)   # T: list -> tuple

            if new_state not in visited:   # 4. CHECK visited
                visited.add(new_state)
                queue.append((new_state, path + [state]))   # 5. APPEND to back

    return None   # queue empty = no solution


# Initial puzzle
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = bfs(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found")