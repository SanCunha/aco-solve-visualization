import pygame
from utils import euclidean_distance, normalize_pheromones


class PygameRenderer:
    def __init__(self, width, height, font_size):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, font_size)
        self.width = width
        self.height = height

    def draw_points(self, points):
        for i, point in enumerate(points):
            pygame.draw.circle(self.screen, (255, 0, 0), (point.x, point.y), 5)
            label = self.font.render(str(i), True, (255, 255, 255))
            self.screen.blit(label, (point.x + 5, point.y + 5))

    def draw_pheromones(self, points, pheromones):
        normalized_pheromones = normalize_pheromones(pheromones)
        pheromone_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    pheromone_level = normalized_pheromones[i][j]
                    if pheromone_level > 0:
                        color = (0, 255, 0, int(pheromone_level * 255))
                        pygame.draw.line(
                            pheromone_surface,
                            color,
                            (points[i].x, points[i].y),
                            (points[j].x, points[j].y),
                            2,
                        )
        self.screen.blit(pheromone_surface, (0, 0))

    def draw_best_path(self, best_path):
        best_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        for i in range(len(best_path) - 1):
            pygame.draw.line(
                best_surface,
                (0, 0, 255),
                (best_path[i].x, best_path[i].y),
                (best_path[i + 1].x, best_path[i + 1].y),
                3,
            )
        self.screen.blit(best_surface, (0, 0))

    def display_info(self, points, best_distance, best_path):
        best_distance_text = self.font.render(
            f"Melhor Distância: {best_distance:.2f}",
            True,
            (255, 255, 255),
        )
        best_path_text = self.font.render(
            f"Melhor rota: {[points.index(p) for p in best_path]}",
            True,
            (255, 255, 255),
        )

        self.screen.blit(best_distance_text, (10, 10))
        self.screen.blit(best_path_text, (10, 30))

    def update_display(self):
        pygame.display.flip()
        self.clock.tick(30)

    def clear_screen(self):
        self.screen.fill((0, 0, 0))
