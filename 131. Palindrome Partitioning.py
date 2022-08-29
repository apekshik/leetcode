from pydoc import ispackage
from typing import List

class Solution:
    # basic palindrome checker. WORKS
    def isPalindrome(self, s) -> bool:
        for i in range(int(len(s) / 2)):
            if s[i] != s[len(s) - i - 1]:
                return False 
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        pb = []

        # a backtracking dfs algorithm. 
        def dfs(str):
            if not str: 
                res.append(pb.copy())
                return 
            
            for i in range(1, len(str) + 1):
                substr1 = str[0:i]
                if self.isPalindrome(substr1):
                    pb.append(substr1)
                    dfs(str[i:])
                    pb.pop()
        dfs(s)
        return res

S = Solution()
print(S.partition("aa"))