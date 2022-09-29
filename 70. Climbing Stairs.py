class Solution:
    def climbStairs(self, n: int) -> int:
        one, two, temp = 1, 1, 1

        for i in range(n-1):
            temp = one + two
            two = one 
            one = temp

        return temp 
        
S = Solution()
print(S.climbStairs(2))