import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = []
        self.assertEqual(Solution().letterCombinations(Input),Output);

class Solution():
    def letterCombinations(self, digits):
        if digits == "":
            return []
        return None

if __name__ == '__main__':
    unittest.main()
