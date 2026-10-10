import random
import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

display_info = screen.get_size()
screen_width = display_info[0]
screen_height = display_info[1]

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)

particle_count = 50


class Particle:
    def __init__(self, screen_size):
        self.radius = random.randint(1, 3)
        self.x = random.randint(-50, screen_size[0] - self.radius)
        self.y = random.randint(-50, screen_size[1] - self.radius)
        self.pos = (self.x, self.y)
        self.speed_x = random.randint(3, 6)
        self.speed_y = random.randint(3, 6)

    def draw(self, window):
        pygame.draw.circle(window, white, self.pos, self.radius)

    def function(self):
        self.x += self.speed_x
        self.y += self.speed_y

        self.radius += 0.01
        self.radius = round(self.radius, 1)

        self.pos = (self.x, self.y)

    def update(self, window):
        self.draw(window)
        self.function()


particles = []
for _ in range(particle_count):
    particle = Particle(display_info)
    particles.append(particle)


def draw(window, screen_size):
    screen.fill(black)

    for p in particles[:]:
        if (p.x >= screen_size[0] + p.radius) or (p.radius >= screen_size[1] + 100):
            particles.remove(p)
        p.update(window)

    if len(particles) < particle_count:
        p_ = Particle(screen_size)
        particles.append(p_)

    pygame.display.update()


def main():
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        draw(screen, display_info)


if __name__ == '__main__':
    main()
