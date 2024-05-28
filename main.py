import pygame
import random
from point import Point
from ant_colony_optimizer import AntColonyOptimizer
from pygame_renderer import PygameRenderer

# Configs
WIDTH, HEIGHT = 800, 600
NUM_ANTS = 10
NUM_POINTS = 25
NUM_GENERATIONS = 20
EVAPORATION_RATE = 0.01
ALPHA = 1.0
BETA = 2.0
Q = 100.0
MUTATION_RATE = 0.1
FONT_SIZE = 24

# Random Points
points = [
    Point(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    for _ in range(NUM_POINTS)
]

# Inicialization
aco = AntColonyOptimizer(
    points, NUM_ANTS, ALPHA, BETA, EVAPORATION_RATE, Q, MUTATION_RATE
)
renderer = PygameRenderer(WIDTH, HEIGHT, FONT_SIZE)
aco.initialize_population()

# Main
running = True
best_distance = float("inf")
best_path = []

while running:
    renderer.clear_screen()
    renderer.draw_points(points)
    renderer.update_display()

    for generation in range(NUM_GENERATIONS):
        best_ant = aco.run_generation()

        if best_ant.distance < best_distance:
            best_distance = best_ant.distance
            best_path = best_ant.path

        renderer.draw_points(points)
        renderer.draw_pheromones(points, aco.pheromones)
        renderer.draw_best_path(best_path)
        renderer.display_info(points, best_distance, best_path)
        renderer.update_display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
