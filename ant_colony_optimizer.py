import random
from utils import euclidean_distance, two_opt, evaluate_ant_path
from ant import Ant


class AntColonyOptimizer:
    def __init__(
        self, points, num_ants, alpha, beta, evaporation_rate, q, mutation_rate
    ):
        self.points = points
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.q = q
        self.mutation_rate = mutation_rate
        self.pheromones = [
            [1.0 for _ in range(len(points))] for _ in range(len(points))
        ]
        self.population = []

    def initialize_population(self):
        self.population = []
        for _ in range(self.num_ants):
            path = random.sample(self.points, len(self.points))
            path.append(path[0])
            distance = evaluate_ant_path(path)
            self.population.append(Ant(path, distance))

    def select_parents(self):
        tournament_size = 5
        parents = []
        for _ in range(2):
            tournament = random.sample(self.population, tournament_size)
            parent = min(tournament, key=lambda ant: ant.distance)
            parents.append(parent)
        return parents

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1.path) - 2)
        child_path1 = parent1.path[:crossover_point] + [
            p for p in parent2.path if p not in parent1.path[:crossover_point]
        ]
        child_path2 = parent2.path[:crossover_point] + [
            p for p in parent1.path if p not in parent2.path[:crossover_point]
        ]
        return child_path1, child_path2

    def mutate(self, path):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(1, len(path) - 1), 2)
            path[i], path[j] = path[j], path[i]
        return path

    def update_pheromones(self, best_ants):
        for i in range(len(self.points)):
            for j in range(len(self.points)):
                self.pheromones[i][j] *= 1 - self.evaporation_rate

        for ant in best_ants:
            for k in range(len(ant.path) - 1):
                i = self.points.index(ant.path[k])
                j = self.points.index(ant.path[k + 1])
                self.pheromones[i][j] += self.q / ant.distance
                self.pheromones[j][i] += self.q / ant.distance

    def run_generation(self):
        for ant in self.population:
            ant.distance = evaluate_ant_path(ant.path)

        new_population = []
        for _ in range(self.num_ants // 2):
            parent1, parent2 = self.select_parents()
            child_path1, child_path2 = self.crossover(parent1, parent2)
            child_path1 = self.mutate(child_path1)
            child_path2 = self.mutate(child_path2)
            child_path1.append(child_path1[0])
            child_path2.append(child_path2[0])
            new_population.append(Ant(child_path1, evaluate_ant_path(child_path1)))
            new_population.append(Ant(child_path2, evaluate_ant_path(child_path2)))

        for ant in new_population:
            ant.path = two_opt(ant.path)
            ant.distance = evaluate_ant_path(ant.path)

        self.population = new_population

        best_ants = sorted(self.population, key=lambda ant: ant.distance)[:10]
        self.update_pheromones(best_ants)

        return min(self.population, key=lambda ant: ant.distance)
