from typing import List # is used for py3.8 and earlier for List type hinting. 
# 3.9+ you can use list[int] and so on without the typing import. 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        