import unittest
from CodilityPractice.lessons.lesson_1 import binary_gap
from CodilityPractice.lessons.lesson_2 import cycle_array


class TestLesson1(unittest.TestCase):

    def test_l1(self):

        self.assertEqual(binary_gap(1041), 5)
        self.assertEqual(binary_gap(31), 0)

        self.assertRaises(AssertionError, binary_gap, -1)
        self.assertRaises(AssertionError, binary_gap, 0.1)
        self.assertRaises(AssertionError, binary_gap, [1, 2])
        self.assertRaises(AssertionError, binary_gap, (1, 2))
        self.assertRaises(AssertionError, binary_gap, None)


class TestLesson2(unittest.TestCase):

    def test_l2(self):

        self.assertEqual(cycle_array([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(cycle_array([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(cycle_array([1, 2, 3, 4], 4), [1, 2, 3, 4])

        self.assertRaises(AssertionError, cycle_array, 1, 1)
        self.assertRaises(AssertionError, cycle_array, [1, 2], [1, 2])
        self.assertRaises(AssertionError, cycle_array, 1, None)
        self.assertRaises(AssertionError, cycle_array, None, 1)
        self.assertRaises(AssertionError, cycle_array, -1, 1)
        self.assertRaises(AssertionError, cycle_array, 1, -1)
        self.assertRaises(AssertionError, cycle_array, (1, 2), 1)
        self.assertRaises(AssertionError, cycle_array, 1, (2, 1))



