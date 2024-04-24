import unittest
from media import calcular_media

class TestCalcularMedia(unittest.TestCase):

    def test_media_de_dois_numeros_positivos(self):
        self.assertEqual(calcular_media(3, 5), 4)

    def test_media_de_um_numero_positivo_e_um_numero_negativo(self):
        self.assertEqual(calcular_media(4, -2), 1)

    def test_media_de_dois_numeros_negativos(self):
        with self.assertRaises(ValueError):
            calcular_media(-1, -3)

if __name__ == '__main__':
    unittest.main()
