import UFraction
import unittest
import random


class TestUFraction(unittest.TestCase):
    def test_init_eq(self):
        self.assertEqual(UFraction.UFraction(10, 20), UFraction.UFraction(1, 2))
        self.assertEqual(UFraction.UFraction(123, 123), UFraction.UFraction(2, 2))
        self.assertEqual(UFraction.UFraction(1.23, 1.4), UFraction.UFraction(123, 140))
        self.assertEqual(UFraction.UFraction(-0.2, 1), UFraction.UFraction(-2, 10))
        self.assertEqual(UFraction.UFraction(4, 2), 2)

    def test_compares(self):
        self.assertEqual(UFraction.UFraction(1, 2) < 1, True)
        self.assertEqual(UFraction.UFraction(1, 2) <= 1, True)
        self.assertEqual(UFraction.UFraction(2, 2) <= 1, True)
        self.assertEqual(1 > UFraction.UFraction(1, 2), True)
        self.assertEqual(UFraction.UFraction(10, 2) > 4, True)
        self.assertEqual(UFraction.UFraction(10, 2) >= 4, True)
        self.assertEqual(UFraction.UFraction(10, 2) > 5, False)
        self.assertEqual(UFraction.UFraction(10, 2) >= 5, True)

    def test_str(self):
        self.assertEqual(repr(UFraction.UFraction(10, 20)), "Upgraded fraction, numerator = 1, denominator = 2")
        self.assertEqual(repr(UFraction.UFraction(123, 123)), "Upgraded fraction, numerator = 1, denominator = 1")

    def test_add(self):
        self.assertEqual((UFraction.UFraction(10, 20) + UFraction.UFraction(40, 30)),
                         UFraction.UFraction(11, 6))
        self.assertEqual((UFraction.UFraction(10, 20) + UFraction.UFraction(40, 160)),
                         UFraction.UFraction(3, 4))
        self.assertEqual((UFraction.UFraction(1, 3) + UFraction.UFraction(1, 49393)),
                         UFraction.UFraction(49396, 148179))
        self.assertEqual(UFraction.UFraction(1, 2) + 10, UFraction.UFraction(21, 2))
        self.assertEqual(10 + UFraction.UFraction(1, 2), UFraction.UFraction(21, 2))

    def test_multiply(self):
        self.assertEqual((UFraction.UFraction(10, 20) * UFraction.UFraction(40, 160)),
                         UFraction.UFraction(1, 8))
        self.assertEqual((UFraction.UFraction(1, 3) * UFraction.UFraction(1, 49393)),
                         UFraction.UFraction(1, 148179))
        self.assertEqual(3 * UFraction.UFraction(1, 3), 1)
        self.assertEqual(UFraction.UFraction(1, 3) * 4, UFraction.UFraction(4, 3))

    def test_div(self):
        numerator1 = random.randint(1, 1000000)
        denominator1 = random.randint(1, 100000)
        numerator2 = random.randint(1, 100000)
        denominator2 = random.randint(1, 100000)
        self.assertEqual(UFraction.UFraction(numerator1, denominator1) / UFraction.UFraction(numerator2, denominator2),
                         UFraction.UFraction(numerator1, denominator1) * UFraction.UFraction(denominator2, numerator2))
        self.assertEqual(UFraction.UFraction(1, 2) / UFraction.UFraction(1, 2), UFraction.UFraction(1))
        self.assertEqual(UFraction.UFraction(1, 2) / UFraction.UFraction(3, 4), UFraction.UFraction(2, 3))
        self.assertEqual(1 / UFraction.UFraction(3, 4), UFraction.UFraction(4, 3))
        self.assertEqual(3 / UFraction.UFraction(3, 4), UFraction.UFraction(4, 1))

    def test_abs(self):
        self.assertEqual(abs(UFraction.UFraction(-1, -100)), UFraction.UFraction(1, 100))
        self.assertEqual(abs(UFraction.UFraction(-1, 100)), UFraction.UFraction(1, 100))
        self.assertEqual(abs(UFraction.UFraction(1, 100)), UFraction.UFraction(1, 100))

    def test_pow(self):
        self.assertEqual(UFraction.UFraction(10, 11) ** 2, UFraction.UFraction(100, 121))
        self.assertEqual(UFraction.UFraction(2, 3) ** 3, UFraction.UFraction(8, 27))
        self.assertEqual(UFraction.UFraction(2, -3) ** 3, UFraction.UFraction(-8, 27))

    def test_execute(self):
        self.assertEqual(UFraction.UFraction(2, 3).execute(), 2 / 3)
        self.assertEqual(UFraction.UFraction(41, 82).execute(), 1 / 2)
        self.assertEqual(UFraction.UFraction(11, 28).execute(), 11 / 28)

    def test_convert(self):
        self.assertEqual(UFraction.UFraction(1, 3), UFraction.UFraction.convert_from_periodic("0.(3)"))
        self.assertEqual(UFraction.UFraction(7, 9), UFraction.UFraction.convert_from_periodic("0.(7)"))
        self.assertEqual(UFraction.UFraction(185389, 166665), UFraction.UFraction.convert_from_periodic("1.1(12345)"))


if __name__ == '__main__':
    unittest.main()
