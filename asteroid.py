import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ang = random.uniform(20, 50)
        ast_1 = self.velocity.rotate(ang)
        ast_2 = self.velocity.rotate(-ang)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_1.velocity = ast_1
        new_ast_2.velocity = ast_2


