goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

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


def dfs(start, max_depth=12):
    stack = [(start, [])]          # to-do list
    visited = set([start])         # seen-it list

    while stack:
        state, path = stack.pop()          # 1. POP from back

        if state == goal:                  # 2. GOAL?
            return path + [state]

        if len(path) >= max_depth:         # 3. TOO DEEP?
            continue

        zero = state.index(0)              # 4. FIND blank

        for move in moves[zero]:
            new_state = list(state)        # L
            new_state[zero], new_state[move] = new_state[move], new_state[zero]   # S
            new_state = tuple(new_state)   # T

            if new_state not in visited:   # 5. CHECK visited
                visited.add(new_state)
                stack.append((new_state, path + [state]))   # 6. PUSH

    return None


start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)

solution = dfs(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found")