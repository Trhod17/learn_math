import unittest
from learn_math import (
    teacher_addition,
    teacher_subtraction,
    teacher_multiplication,
    teacher_division,
    addition,
    subtraction,
    multiplication,
    division,
)


class TestTeacherArithmetic(unittest.TestCase):
    def test_teacher_addition(self):
        self.assertEqual(teacher_addition([1, 2]), 3)
        self.assertEqual(teacher_addition([-1, 2]), 1)
        self.assertEqual(teacher_addition([-1, -2, 6]), 3)
        self.assertEqual(teacher_addition([1.5, 2.2]), 3.7)
        self.assertEqual(teacher_addition([1, 0]), 1)

    def test_teacher_subtraction(self):
        self.assertEqual(teacher_subtraction([3, 1]), 2)

    def test_teacher_multiplication(self):
        self.assertEqual(teacher_multiplication([3, 5]), 15)

    def test_teacher_division(self):
        self.assertAlmostEqual(teacher_division([3.0, 2]), 1.5)


"""  Uncomment this class to test student's work.
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
"""


if __name__ == "__main__":
    unittest.main()
