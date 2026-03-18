import unittest
from personaje import Personaje
from equipo import Equipo


class TestPersonaje(unittest.TestCase):

    def test_subir_nivel(self):
        p = Personaje("Arthos", "guerrero", 1, 10, 30)

        p.subir_nivel()

        self.assertEqual(p.nivel, 2)
        self.assertEqual(p.ataque, 12)
        self.assertEqual(p.vida, 35)

    def test_esta_vivo(self):
        p = Personaje("Luna", "maga", 3, 8, 20)

        self.assertTrue(p.esta_vivo())

        p.recibir_dano(25)

        self.assertFalse(p.esta_vivo())


class TestEquipo(unittest.TestCase):

    def test_agregar_personaje(self):
        equipo = Equipo()
        p = Personaje("Ragnar", "guerrero", 5, 15, 40)

        equipo.agregar(p)

        self.assertEqual(len(equipo.personajes), 1)

    def test_eliminar_personaje(self):
        equipo = Equipo()

        p1 = Personaje("Ragnar", "guerrero", 5, 15, 40)
        p2 = Personaje("Merlin", "mago", 4, 12, 25)

        equipo.agregar(p1)
        equipo.agregar(p2)

        equipo.eliminar("Ragnar")

        self.assertEqual(len(equipo.personajes), 1)
        self.assertEqual(equipo.personajes[0].nombre, "Merlin")

    def test_buscar_por_clase(self):
        equipo = Equipo()

        equipo.agregar(Personaje("Ragnar", "guerrero", 5, 15, 40))
        equipo.agregar(Personaje("Arthos", "guerrero", 3, 10, 30))
        equipo.agregar(Personaje("Merlin", "mago", 4, 12, 25))

        guerreros = equipo.buscar_por_clase("guerrero")

        self.assertEqual(len(guerreros), 2)

    def test_ordenar_por_nivel(self):
        equipo = Equipo()

        equipo.agregar(Personaje("A", "guerrero", 5, 10, 30))
        equipo.agregar(Personaje("B", "mago", 2, 8, 20))
        equipo.agregar(Personaje("C", "ladron", 4, 9, 25))

        ordenados = equipo.ordenar_por_nivel()

        self.assertEqual(ordenados[0].nivel, 2)
        self.assertEqual(ordenados[-1].nivel, 5)

    def test_media_nivel(self):
        equipo = Equipo()

        equipo.agregar(Personaje("A", "guerrero", 2, 10, 30))
        equipo.agregar(Personaje("B", "mago", 4, 8, 20))

        self.assertAlmostEqual(equipo.media_nivel(), 3)


if __name__ == "__main__":
    unittest.main()