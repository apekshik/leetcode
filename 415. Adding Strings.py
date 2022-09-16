class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """ 
        "11" = "1" + "1" = 1 * 10^1 + 1 * 10^0 = 11
        "123" = "1" + "2" + "3" = 1 * 10^2 + 2 * 10^1 + 10^0 = 123
        sum = 134
        temp = 134 % 100 this keeps 34
        temp2 = 134 / 100 this keeps 1 
        append temp2 to the result string. 
        repeat process until all digits have been converted to the string form. 
        return result. 
        """
        if (num1 == "0" and num2 == "0"):
            return "0"
    
        sum = 0
        for i in range(len(num1) - 1, -1, -1):
            #print(i)
            d = int(num1[len(num1) - i - 1])
            sum += d * pow(10, i) 
        #print(sum)
        # sum now has num1 in integer form. 
        # we do the same for num2

        for i in range(len(num2) - 1, -1, -1):
            #print(i)
            d = int(num2[len(num2) - i - 1])
            #print(d)
            sum += d * pow(10, i) 
        print(sum) 
        # now sum has num1 + num2 in integer form. 
        # we now convert sum to its string form. 
        res = ""
        stack = [] 
        while sum != 0: 
            stack.append(sum % 10) 
            sum = int(sum / 10) # 
        
        print(stack) 
        while len(stack) != 0:
            res += str(stack.pop())
        
        return res 
            
            
            
            