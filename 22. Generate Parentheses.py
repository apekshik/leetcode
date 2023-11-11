from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we use a backtracking algorithm to generate valid states. 
        # we stop the recursion via the base case: 
        # openCount == closedCount == n. 
        # we cotrol the flow of recursion based on closeCount < openCount.

        stack = [] # to generate the intermediate valid states. 
        res = [] # to store all valid solutions. 

        def backtrack(openCount: int, closedCount: int) -> None:
            # base case. no need to go any further. We've reached the final depth of recursion.
            if openCount == closedCount == n:
                res.append("".join(stack))
                return 
            
            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1, closedCount)
                stack.pop() # clean up the stack for backtracking since it's a global variable.

            if closedCount < openCount:
                stack.append(')')
                backtrack(openCount, closedCount + 1)
                stack.pop() # clean up again for the same reason.  
                
        backtrack(0, 0)
        return res 


''' Alternative Magical Solution without using stack (I came up with it)'''

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # has to be backtracking. We use a stringbuilder variable to store the 
#         # currently created string. We return once the stringbuildder length is twice n. 
#         res = []
#         sb = ''
#         def rec(sb, leftParenthesesLeft, rightParenthesesLeft):
#             # base case
#             if len(sb) == n * 2: 
#                 res.append(sb)
#                 sb = sb[:-1]
#                 return 
#             # recursive step
#             if leftParenthesesLeft > 0: 
#                 rec(sb + '(', leftParenthesesLeft-1, rightParenthesesLeft)
#             if rightParenthesesLeft > 0 and rightParenthesesLeft > leftParenthesesLeft: 
#                 rec(sb + ')', leftParenthesesLeft, rightParenthesesLeft-1)

#         rec(sb, n, n)

#         return res 

# S = Solution() 

# print(S.generateParenthesis(3))