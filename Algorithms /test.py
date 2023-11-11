from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # has to be backtracking. We use a stringbuilder variable to store the 
        # currently created string. We return once the stringbuildder length is twice n. 
        res = []
        sb = ''
        def rec(sb, leftParenthesesLeft, rightParenthesesLeft):
            # base case
            if len(sb) == n * 2: 
                res.append(sb)
                sb = sb[:-1]
                return 
            # recursive step
            if leftParenthesesLeft > 0: 
                rec(sb + '(', leftParenthesesLeft-1, rightParenthesesLeft)
            if rightParenthesesLeft > 0 and rightParenthesesLeft > leftParenthesesLeft: 
                rec(sb + ')', leftParenthesesLeft, rightParenthesesLeft-1)

        rec(sb, n, n)

        return res 

S = Solution() 

print(S.generateParenthesis(3))