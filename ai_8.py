# Import required libraries
import itertools
import math

# Store the coordinates of each city
cities = {
    0: (0, 0),
    1: (2, 4),
    2: (5, 2),
    3: (6, 6),
    4: (1, 5)
}


# Euclidean distance between two cities
def distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Total distance of a route (including return to start)
def path_length(path):
    total = 0
    for i in range(len(path)):
        total += distance(path[i], path[(i + 1) % len(path)])
    return total


# Brute-force Travelling Salesman Problem
def solve_tsp():
    city_ids = list(cities.keys())
    start = city_ids[0]              # fix city 0 as start
    rest = city_ids[1:]              # remaining cities

    best_path = None
    best_length = float('inf')

    for perm in itertools.permutations(rest):    # every ordering
        path = [start] + list(perm)              # full route
        length = path_length(path)               # measure it

        if length < best_length:                 # shorter than best so far?
            best_length = length
            best_path = path

    return best_path, best_length


best_path, best_length = solve_tsp()

print("Best route:", best_path + [best_path[0]])
print("Total distance:", round(best_length, 2))