```python
import math
from src.utils import rotate_point, translate_point

class Wheel:
    def __init__(self, center, radius, num_sides):
        self.center = center
        self.radius = radius
        self.num_sides = num_sides
        self.vertices = self.calculate_vertices()
        self.contact_vertex_index = 0

    def calculate_vertices(self):
        angle_step = 2 * math.pi / self.num_sides
        vertices = []
        for i in range(self.num_sides):
            angle = i * angle_step
            vertex = (self.center[0] + self.radius * math.cos(angle),
                      self.center[1] + self.radius * math.sin(angle))
            vertices.append(vertex)
        return vertices

    def rotate(self, angle):
        self.vertices = [rotate_point(vertex, self.center, angle) for vertex in self.vertices]
        self.contact_vertex_index = (self.contact_vertex_index + 1) % self.num_sides

    def translate(self, distance):
        self.center = translate_point(self.center, distance)
        self.vertices = [translate_point(vertex, distance) for vertex in self.vertices]

    def roll(self):
        # Calculate the rotation angle
        interior_angle = (self.num_sides - 2) * 180 / self.num_sides
        rotation_angle = 180 - interior_angle

        # Rotate the wheel
        self.rotate(rotation_angle)

        # Calculate the translation distance
        side_length = 2 * self.radius * math.sin(math.pi / self.num_sides)
        translation_distance = (0, side_length)

        # Translate the wheel
        self.translate(translation_distance)
```