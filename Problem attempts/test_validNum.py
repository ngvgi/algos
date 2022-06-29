import unittest
import validNum

class TestSolution(unittest.TestCase):
    def test_singleDigitNum(self):
        self.assertFalse(validNum.Solution().validNum('+7'))    
        self.assertFalse(validNum.Solution().validNum('-4'))    
        self.assertFalse(validNum.Solution().validNum('.9'))    
        self.assertTrue(validNum.Solution().validNum('2'))
    
    # def test_integers(self):
    #     self.assertTrue(validNum.Solution().validNum('0089'))
    #     self.assertTrue(validNum.Solution().validNum('0089'))
    #     self.assertTrue(validNum.Solution().validNum('+3.14'))


if __name__ == '__main__':
    unittest.main()