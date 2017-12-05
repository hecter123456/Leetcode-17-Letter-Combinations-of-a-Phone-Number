import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = ""
        Output = []
        self.assertEqual(Solution().letterCombinations(Input),Output);
    def testOnlyOneNumber(self):
        Input = "2"
        Output = ["a","b","c"]
        self.assertEqual(Solution().letterCombinations(Input),Output);

class Solution():
    def letterCombinations(self, digits):
        if digits == "":
            return []
        dic = {"1" : ["*"],
               "2" : ["a","b","c"],
               "3" : ["d","e","f"],
               "4" : ["g","h","i"],
               "5" : ["j","k","l"],
               "6" : ["m","n","o"],
               "7" : ["p","q","r","s"],
               "8" : ["t","u","v"],
               "9" : ["w","x","y","z"],
               "0" : [" "]}
        ans = []
        for item in digits:
            for dicitem in dic[item]:
                ans.append(dicitem)

        return ans

if __name__ == '__main__':
    unittest.main()
