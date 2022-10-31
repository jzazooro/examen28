from ejercicio2.pregunta2 import determinateiterativo
import unittest

class test2(unittest.TestCase):

    def primertest(self):
        self.assertEqual(determinateiterativo(1, 56, 19, 9, 11, 67, 0, 13, 88), -42032.0)

    def segundotest(self):
        self.assertEqual(determinateiterativo(4, 6, 129, 229, 1, 0, 8, 99, 9), 2911197.0)

if __name__ == '__main__':
    unittest.main()