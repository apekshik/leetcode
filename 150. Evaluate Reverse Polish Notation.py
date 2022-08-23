# 150. Evaluate Reverse Polish Notation
# It is guaranteed that the given RPN expression is always valid. 
# That means the expression would always evaluate to a result, 
# and there will not be any division by zero operation.

'''
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens: 
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: 
                stack.append(int(c))
        
        return stack.pop()