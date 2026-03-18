import unittest
import estadistica


class TestEstadistica(unittest.TestCase):

    def test_media(self):
        self.assertEqual(estadistica.media([2, 4, 6]), 4)
        self.assertAlmostEqual(estadistica.media([1, 2]), 1.5)

    def test_mediana(self):
        self.assertEqual(estadistica.mediana([1, 3, 5]), 3)
        self.assertAlmostEqual(estadistica.mediana([1, 2, 3, 4]), 2.5)

    def test_rango_intercuartilico(self):
        self.assertEqual(estadistica.rango_intercuartilico([1,2,3,4,5,6,7,8]), 4)
        self.assertTrue(estadistica.rango_intercuartilico([10,20,30,40,50,60,70,80]) > 0)

    def test_dispersion(self):
        self.assertEqual(estadistica.dispersion([1,2,3,4,5]), 4)
        self.assertFalse(estadistica.dispersion([5,5,5,5]) > 0)


if __name__ == "__main__":
    unittest.main()