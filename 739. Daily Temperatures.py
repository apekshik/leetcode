class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 

        # each element of stack is a pair of the temp value and its index in the original array. 
        stack = [] # pair: [temp, index]

        for i, t in enumerate(temperatures): 
            while stack and t > stack[-1][0]: 
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])

        return res  