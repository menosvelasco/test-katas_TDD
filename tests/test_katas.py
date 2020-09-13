import unittest
import katas
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(10, 90), 100)
        self.assertEqual(katas.add(-5, 10), 5)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 8), 16)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)

    def test_factorial(self):
        self.assertIsNotNone(katas.factorial)
        self.assertEqual(katas.factorial(4), math.factorial(4))
        for x in range(10):
            self.assertEqual(katas.factorial(x), math.factorial(x))

    def test_fibonacci(self):
        list_fib = [
            0,	1,	1,	2,	3,	5,	8,	13,	21,	34,	55,	89,	144,
            233, 377, 610, 987, 1597, 2584,	4181,	6765,	10946,	17711, 28657,
            46368, 75025, 121393, 196418, 317811, 514229
        ]

        for index, value in enumerate(list_fib):
            self.assertEqual(katas.fibonacci(index), value)
            self.assertRaises(ValueError, katas.fibonacci, -5)


if __name__ == '__main__':
    unittest.main()
