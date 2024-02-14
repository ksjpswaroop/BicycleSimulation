```python
from wheel import Wheel
from line import Line

class Bicycle:
    def __init__(self, wheel1, wheel2, line):
        self.wheel1 = wheel1
        self.wheel2 = wheel2
        self.line = line

    def move(self, direction, speed):
        # Move the bicycle in the given direction at the given speed
        self.wheel1.move(direction, speed)
        self.wheel2.move(direction, speed)
        self.line.move(direction, speed)

    def rotate_wheels(self, angle):
        # Rotate the wheels by the given angle
        self.wheel1.rotate(angle)
        self.wheel2.rotate(angle)

    def update(self):
        # Update the state of the bicycle
        self.move(self.direction, self.speed)
        self.rotate_wheels(self.angle)

    def draw(self):
        # Draw the bicycle
        self.wheel1.draw()
        self.wheel2.draw()
        self.line.draw()
```