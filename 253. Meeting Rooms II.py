# Definition of Interval. 
class Interval(object):
    def __init__(self, start, end):
        self.start = start 
        self.end = end 

class Solution: 
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals]) 

        res, count = 0, 0 # count stores room count at each point in time. 
        s, e = 0, 0 # s is the start pointer and e is the end pointer. 

        while s < len(intervals):
            if start[s] < start[e]:
                s += 1
                count += 1
            else: 
                e += 1
                count -= 1
            res = min(res, count)

        return res 




