import unittest
from Analysis.beam_patterning import load_pattern


class TestFunctions(unittest.TestCase):
    def test_load_pattern(self):
        self.assertEqual(load_pattern(1), [[1]])
        self.assertEqual(load_pattern(2), [[1, 1], [0, 1], [1, 0]])



if __name__ == '__main__':
    unittest.main()
