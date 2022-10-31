from ejercicio2.pregunta2 import determinateiterativo
from ejercicio2.pregunta2 import determinanterecursivo
import unittest

class test2(unittest.TestCase):

    def setUp(cls):
        cls.matriz=[[1, 56, 19], [9, 11, 67], [0, 13, 88]]
        cls.matrizdos=[[4, 6, 129], [229, 1, 0], [8, 99, 9]]

    def primertest(self):
        self.assertEqual(determinateiterativo(1, 56, 19, 9, 11, 67, 0, 13, 88))

    def segundotest(self):
        self.assertEqual(determinateiterativo(4, 6, 129, 229, 1, 0, 8, 99, 9))

    def tercertest(self):
        self.assertEqual(determinanterecursivo(self.matriz, 0, 0))

    def cuartotest(self):
        self.assertEqual(determinanterecursivo(self.matrizdos, 0, 0))

if __name__ == '__name__':
    unittest.main()