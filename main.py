# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)

    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()
    black = 0, 0, 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return

        screen.fill(black)
        dt = clock.tick(60) / 1000
        for sprite in drawable:
            sprite.draw(screen)
        
        for sprite in updatable:
            sprite.update(dt)

            
        pygame.display.flip()
             


if __name__ == "__main__":
	main()
