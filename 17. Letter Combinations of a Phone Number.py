from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 

        map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        s = len(digits)
        def dfs(digits, sb):
            if len(sb) == s:
                res.append(sb)
                return 
            for l in map[digits[0]]:
                sb += l
                dfs(digits[1:], sb)
                sb = sb[:-1]
        dfs(digits, "")
        return res   

S = Solution()

print(S.letterCombinations("23"))