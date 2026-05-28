import unittest
from geometry import triangle_area, square_area


class TestGeometry(unittest.TestCase):

    def test_triangle(self):
        # Verification: If base=10 and height=5, area must be 25.0
        self.assertEqual(triangle_area(10, 5), 25.0)

    def test_square(self):
        # Verification: If side=4, area must be 16
        self.assertEqual(square_area(4), 16)


if __name__ == "__main__":
    unittest.main()
