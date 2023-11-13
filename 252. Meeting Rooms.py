class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        # take all the times (both start and end and sort them in order)
        # Keep a mapping of whether each time is a start or end. 
        
        # make a dictionary where the key is the time and the value tells us whether it is a start time or end time. 
        
        # sort the dictionary by time and iterate through it incremementing and decrementing based on start or end time 
        
        # create dictionary. 
        times = [] 
        for meeting in A: 
            times.append([meeting[0], 'start'])
            times.append([meeting[1], 'end'])
            
        # sort the dictionary 
        sortedTimes = sorted(times, key=lambda items: (items[0], items[1]))
        # print(sortedTimes)
        # keep a counter for roomms 
        cnt = 0 
        mxCnt = 0
        for time, se in sortedTimes: 
            if se == 'start': 
                # print("new meeting room opened")
                cnt += 1
                mxCnt = max(mxCnt, cnt)
            else: 
                # print("closed meeting room")
                cnt -= 1
                mxCnt = max(mxCnt, cnt)
        
        return mxCnt 
                