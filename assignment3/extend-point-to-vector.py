import math

class Point:
    """A point in 2D space"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x, self.y})"

    def distance_to(self, other):
        """Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)

class Vector(Point):
    """A 2D vector. Inherits __init__, __eq__, and distance_to from Point."""

    def __repr__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    print("=== Point ===")
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(3, 4)
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p2 == p3: {p2 == p3}")
    print(f"Distance p1 -> p2: {p1.distance_to(p2)}")
    print(f"Distance p2 -> p3: {p2.distance_to(p3)}")

    print("\n=== Vector ===")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = Vector(1, 2)
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 == v3: {v1 == v3}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"Distance v1 -> v2: {v1.distance_to(v2):.4f}")

    v_sum = v1 + v2
    print(f"v1 + v2 = {v_sum}")
    print(f"Type of sum: {type(v_sum).__name__}")

    print("\n=== Inheritance checks ===")
    print(f"Vector is a Point: {isinstance(v1, Point)}")
    print(f"Point vs Vector printing: {p2} vs {v2}")
    print(f"Distance from Point to Vector: {p1.distance_to(v2):.4f}")