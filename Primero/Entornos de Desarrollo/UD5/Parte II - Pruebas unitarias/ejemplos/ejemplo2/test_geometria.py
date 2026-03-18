import unittest
import math
import geometria


class TestGeometria(unittest.TestCase):

    def test_area_rectangulo(self):
        self.assertEqual(geometria.area_rectangulo(4, 5), 20)
        self.assertEqual(geometria.area_rectangulo(0, 5), 0)
        self.assertEqual(geometria.area_rectangulo(2.5, 4), 10.0)

    def test_area_circulo(self):
        self.assertAlmostEqual(geometria.area_circulo(1), math.pi)
        self.assertAlmostEqual(geometria.area_circulo(0), 0)
        self.assertAlmostEqual(geometria.area_circulo(2), math.pi * 4)

    def test_perimetro_rectangulo(self):
        self.assertEqual(geometria.perimetro_rectangulo(3, 4), 14)
        self.assertEqual(geometria.perimetro_rectangulo(0, 4), 8)

    def test_perimetro_circulo(self):
        self.assertAlmostEqual(geometria.perimetro_circulo(1), 2 * math.pi)
        self.assertAlmostEqual(geometria.perimetro_circulo(0), 0)


if __name__ == "__main__":
    unittest.main()