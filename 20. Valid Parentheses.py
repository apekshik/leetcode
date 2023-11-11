class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        # sets for checking which type of brackets we have (left or right)
        leftSet = {'(', '{', '['}
        rightSet = { ')', '}', ']'}
        # mapping for quick access. 
        rightSideMap = {'(':')', '{':'}', '[':']'}

        for c in s: 
            if c in leftSet: 
                stack.append(c)
            # Dealing with right bracket cases is a bit more subtle. 
            elif c in rightSet: 
                # This if check is to deal with inputs like "]]]" where there isn't any prior left bracket, so the stack 
                # is empty and trying to access elements from it will throw an index error. 
                if stack:
                    # If the top of the stack has the corresponding correct bracket that we're looking at in the input string
                    # then pop stack and move to the next character in the string. 
                    if c == rightSideMap[stack[-1]]: 
                        stack.pop() 
                    else: # otherwise there's a bracket mismatch. No further checking needed. Can return false immediately. 
                        return False
                else: # here we can again return false immedieately since we have a bracket mismatch but of a different kind.
                    return False
        
        # if the stack is empty (no left brackets remain), we've found a good input, so return True. 
        if len(stack) == 0: 
            return True
        
        return False 
    


