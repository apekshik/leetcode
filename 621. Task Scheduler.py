class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = len(tasks)
        
        keys = [key for key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        
        taskCount = dict.fromkeys(keys, 0)
        
        for task in tasks: 
            taskCount[task] += 1
        
        sortDict = sorted(taskCount.items(), key=lambda item: item[1], reverse=True)
        
        maxF = sortDict[0][1]
        idleTimeLeft = n * (maxF - 1)
        totalAvailTime = idleTimeLeft
        temp = 0 # to store how many extra spots are needed after the end of idle time
        
        for i in range(1, 26):
            if sortDict[i][1] == maxF:
                idleTimeLeft -= sortDict[i][1] - 1
                temp += 1
            else:
                idleTimeLeft -= sortDict[i][1]
        
        
        if idleTimeLeft >= 0:
            return maxF + totalAvailTime + temp
        else:
            return maxF + totalAvailTime - idleTimeLeft + temp 
             
        
            