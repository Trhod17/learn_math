import unittest
from learn_math.solutions.arithmetic import (
    addition,
    subtraction,
    multiplication,
    division,
)


class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition([1, 2]), 3)
        self.assertEqual(addition([-1, 2]), 1)
        self.assertEqual(addition([-1, -2, 6]), 3)
        self.assertEqual(addition([1.5, 2.2]), 3.7)
        self.assertEqual(addition([1, 0]), 1)

    def test_subtraction(self):
        self.assertEqual(subtraction([3, 1]), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication([3, 5]), 15)

    def test_division(self):
        self.assertAlmostEqual(division([3.0, 2]), 1.5)


if __name__ == "__main__":
    unittest.main()
