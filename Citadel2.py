def solve(m, s):
    # fill this function
    l1 = [] # list to store ascii number lists for input strings. 
    values = [] # to store values. 
    # convert each string to a list of ascii number equivalents. 
    for st in s: 
        temp = [] # to build the list for each string.
        for c in st: 
            temp.append(ord(c))
        l1.append(temp.copy())
    
    # we can essentially use a DP approach by storing the powers of the 
    # ascii numbers (97-122) and the number of times they appear in each 
    # input string. This will certainly optimize the run time of the program. 
    dp = {} # hashmap to store these values as we talked above. 
    count = 0
    for nl in l1: # for a number list in the list of lists: 
        for num in nl: 
            if num not in dp: 




solve(2, ['abc', 'abcd'])