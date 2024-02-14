```python
import pygame
from animation import animate
from bicycle import Bicycle
from wheel import Wheel
from line import Line

def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set up assets
    WHEEL_IMG = pygame.image.load('assets/bicycle_shape_1.png')
    BICYCLE_IMG = pygame.image.load('assets/bicycle_shape_2.png')

    # Set up bicycle
    wheel1 = Wheel(WHEEL_IMG, (WIDTH / 2, HEIGHT / 2))
    wheel2 = Wheel(WHEEL_IMG, (WIDTH / 2 + 100, HEIGHT / 2))
    line = Line((WIDTH / 2, HEIGHT / 2), (WIDTH / 2 + 100, HEIGHT / 2))
    bicycle = Bicycle(BICYCLE_IMG, wheel1, wheel2, line)

    # Set up clock
    clock = pygame.time.Clock()

    # Run animation
    animate(screen, bicycle, clock)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
```