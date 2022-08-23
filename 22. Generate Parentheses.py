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
