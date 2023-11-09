import heapq 

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums
#         heapq.heapify(self.nums)
#         print(self.nums)
        
        
#     def add(self, val: int) -> int:
#         heapq.heappush(self.nums, val)

#         for i in range(k):
#             heapq.heappop(self.nums)

class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        print("heap array after heapifying:", self.nums)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        heapc = list(self.nums)
         
        for i in range(self.k - 1): 
            heapq.heappop(heapc)
        
        return heapq.heappop(heapc)

nums = [4, 5, 8, 2, 9, 12, 7]
obj = KthLargest(3, nums)
param_1 = obj.add(15)
print(param_1)
param_1 = obj.add(3)
print(param_1)