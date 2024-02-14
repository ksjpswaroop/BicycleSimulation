```python
import math

def calculate_interior_angle(n):
    """
    Calculate the interior angle of a regular polygon with n sides.
    """
    return (n - 2) * 180 / n

def calculate_rotation_angle(n):
    """
    Calculate the rotation angle when a vertex of a regular polygon with n sides hits the ground.
    """
    return 180 - calculate_interior_angle(n)

def calculate_arc_length(s):
    """
    Calculate the arc length when one side of a polygon with side length s rolls onto the ground.
    """
    return s

def rotate_point(point, angle, center):
    """
    Rotate a point counterclockwise by a given angle around a given center.
    """
    angle = math.radians(angle)
    temp_point = point[0] - center[0] , point[1] - center[1]
    rotated_point = temp_point[0]*math.cos(angle) - temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle) + temp_point[1]*math.cos(angle)
    rotated_point = rotated_point[0] + center[0] , rotated_point[1] + center[1]
    return rotated_point

def translate_point(point, dx, dy):
    """
    Translate a point by dx and dy.
    """
    return point[0] + dx, point[1] + dy
```