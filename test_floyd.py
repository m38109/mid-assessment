# tests/test_floyds_recursive.py
import unittest
from floyds_recursive import floyd_recursive_wrapper

No_Path = float('inf')
class TestFloydRecursive(unittest.TestCase):
    def test_shortest_paths(self):
        graph = [
            [0, 3, No_Path, 7],
            [8, 0, 2, No_Path],
            [5, No_Path, 0, 1],
            [2, No_Path, No_Path, 0]
        ]
        expected_result = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, No_Path, 0, 1],
            [2, No_Path, No_Path, 0]
        ]
        self.assertEqual(floyd_recursive_wrapper(graph), expected_result)

if __name__ == '__main__':
    unittest.main()
