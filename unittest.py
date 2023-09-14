# tests/test_floyds_recursive.py
import unittest
from floyds_recursive import floyd_recursive_wrapper

class TestFloydRecursive(unittest.TestCase):
    def test_shortest_paths(self):
        graph = [
            [0, 3, float('inf'), 7],
            [8, 0, 2, float('inf')],
            [5, float('inf'), 0, 1],
            [2, float('inf'), float('inf'), 0]
        ]
        expected_result = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ]
        self.assertEqual(floyd_recursive_wrapper(graph), expected_result)

if __name__ == '__main__':
    unittest.main()
