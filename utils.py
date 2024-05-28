import math


def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def two_opt(path):
    best_path = path[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                if j - i == 1:
                    continue
                new_path = path[:]
                new_path[i:j] = reversed(path[i:j])
                if evaluate_ant_path(new_path) < evaluate_ant_path(best_path):
                    best_path = new_path[:]
                    improved = True
        path = best_path[:]
    return best_path


def evaluate_ant_path(path):
    return sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))


def normalize_pheromones(pheromones):
    max_pheromone = max(max(row) for row in pheromones)
    if max_pheromone == 0:
        return pheromones
    return [[pheromone / max_pheromone for pheromone in row] for row in pheromones]
