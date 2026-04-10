class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        def dfs(r, c):
            # Base case: reached end of board
            if r == 9:
                return True
            
            # Move to next row
            if c == 9:
                return dfs(r + 1, 0)
            
            # Skip empty cells
            if board[r][c] == '.':
                return dfs(r, c + 1)
            
            num = board[r][c]
            box_index = (r // 3) * 3 + (c // 3)
            
            # Check if already seen
            if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                return False
            
            # Mark as seen
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_index].add(num)
            
            # Recurse to next cell
            return dfs(r, c + 1)
        
        return dfs(0, 0)