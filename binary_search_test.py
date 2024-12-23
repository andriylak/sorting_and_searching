import unittest
import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.array = [2, 2, 4, 6, 6, 8, 8, 8, 10, 12, 12, 14]
        self.empty_array = []
        self.single_element_array = [10]

    def RunTestCases(self, method):
        test_cases = [
            (self.array, 8, 5),  # target is in the middle
            (self.array, 10, 8),  # target above the middle
            (self.array, 4, 2),  # target below the middle
            (self.array, 2, 0),  # target at the beginning
            (self.array, 14, 11),  # target at the end
            (self.array, 5, -1),  # target not in array (below middle)
            (self.array, 13, -1),  # target not in array (above middle)
            (self.array, -100, -1),  # target below range
            (self.array, 100, -1),  # target above range
            (self.empty_array, 10, -1),  # empty array
            (self.single_element_array, 10, 0),  # single-element array, target exists
            (self.single_element_array, 5, -1),  # single-element array, target absent
        ]
        for array, target, expected_position in test_cases:
            with self.subTest(array=array, target=target):
                self.assertEqual(method(array, target), expected_position)

    def test_binarySearchIterative(self):
        self.RunTestCases(binary_search.BinarySearch_iterative)

    def test_binarySearchRecursive(self):
        self.RunTestCases(binary_search.BinarySearch_recursive)


if __name__ == "__main__":
    unittest.main(verbosity=2)
