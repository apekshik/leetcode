class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i) -> bool:
            # if i is the length of the given word, it means we reached the 
            # end of the word. So return true.
            if i == len(word):
                return True

            # all of these conditions indicate an incorrect path, so we 
            # return False in all these cases. 
            if (    # order of these OR statements really does matter. 
                    r < 0 or c < 0 or r >= ROWS or c >= COLS or # check outer bounds.
                    word[i] != board[r][c] or # check if curr char matches board char. 
                    (r, c) in path # you essentially looped back onto already searched regions. 
               ):
                return False 

            # since we processed current coordinate on board, add it to path set. 
            path.add((r,c))
            res = (
                    dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1)
                  )
            path.remove((r,c)) # backtrack out of the current path to add new path. 
            return res 

        # check for all coordinates as starting point on board. 
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True 
        return False 