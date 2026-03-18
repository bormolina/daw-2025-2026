import unittest

def area_rectangulo(base: float, altura: float) -> float:
    return base * altura

class TestAreaRectangulo(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area_rectangulo(4, 5), 20)

    def test_area_con_cero(self):
        self.assertEqual(area_rectangulo(0, 5), 0)

    def test_area_con_decimales(self):
        self.assertEqual(area_rectangulo(2.5, 4), 10.0)

if __name__ == "__main__":
    unittest.main()

