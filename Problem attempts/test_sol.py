import unittest
from permutationCheck import solution


class TestCorrectness(unittest.TestCase):
    def perm_SingleVal(self):
        self.assertEqual(solution([1]), 1)
        self.assertEqual(solution([2]), 0)

    def test_TwoElements(self):
        self.assertEqual(solution([2, 3]), 0)
        self.assertEqual(solution([1, 2]), 1)
        self.assertEqual(solution([-22, 1]), 0)

    def test_mixedElementsPosNegFloat(self):
        self.assertEqual(solution([-1, 0.4, 10000000, 2, 3]), 0)

    def test_missingOneVal(self):
        self.assertEqual(solution([4, 3, 2]), 0)

    def test_missingSeveralVals(self):
        self.assertEqual(solution([1, 2, 3, 7]), 0)
        self.assertEqual(solution([1, 2, 3, 7, 4, 5]), 0)
        self.assertEqual(solution([1, 9, 2, 7, 4, 8, 6, 3]), 0)

    def test_perm_allValsPresent(self):
        self.assertEqual(solution([3, 5, 2, 4, 1]), 1)


if __name__ == '__main__':
    unittest.main()
