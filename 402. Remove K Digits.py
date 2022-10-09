
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for c in num:
        while k and stack and stack[-1] > c:
            stack.pop()
            k -= 1
        stack.append(c)
    
    stack = stack[:len(stack) - k]
    res = "".join(stack)
    return str(int(res)) if res else "0"
    ''' my solution. Was close but needed more tweaking to handle edge cases.
    Specifically the one where the entire num is increasing monotonically. 
    # generate our list of numbers from input string.
    nums = [int(x) for x in num]
    # introduce our stack 
    stack = []
    stack.append(nums[0])
    for i in range(1, len(nums)):        
        if not k: 
            stack.append(nums[i])
            continue 

        if nums[i] < stack[-1]:
            stack.pop()
            stack.append(nums[i])
            k -= 1
        else:
            stack.append(nums[i])
    
    res = ""
    switch = 0
    # gets rid of leading 0s. 
    for n in stack:
        if not n and not switch: 
            continue
        res += (str(n))
        switch = 1

    return res
    '''

print(removeKdigits("1432219", 3))
print(removeKdigits("10200", 1))