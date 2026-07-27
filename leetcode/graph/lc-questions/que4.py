# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
 

# Example 1:


# Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
# Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
# Example 2:


# Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
# Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]



from collections import deque

class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        m, n = len(board), len(board[0])
        
        # 1. Helper for 8-way neighbors
        def get_neighbors(r, c):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        yield (nr, nc)

        # 2. Helper to count bombs
        def count_adjacent_mines(r, c):
            count = 0
            for nr, nc in get_neighbors(r, c):
                if board[nr][nc] == 'M':
                    count += 1
            return count

        # 3. BFS function
        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            # Mark as revealed immediately to prevent re-adding to queue
            # We treat 'B' as the revealed blank state
            
            while queue:
                r, c = queue.popleft()
                
                mine_count = count_adjacent_mines(r, c)
                
                if mine_count > 0:
                    # If neighbors have mines, reveal number and STOP expanding
                    board[r][c] = str(mine_count)
                else:
                    # If no mines, reveal as blank and EXPAND to neighbors
                    board[r][c] = 'B'
                    for nr, nc in get_neighbors(r, c):
                        if board[nr][nc] == 'E':
                            # Mark as 'B' before adding to queue to avoid duplicates
                            board[nr][nc] = 'B' 
                            queue.append((nr, nc))

        # --- Main Logic ---
        r, c = click
        
        if board[r][c] == 'M':
            # Rule 1: Clicked on a mine
            board[r][c] = 'X'
        else:
            # Rule 2: Clicked on an empty square
            bfs(r, c)
            
        return board


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    expected = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    board2 = [row[:] for row in expected]
    expected2 = [row[:] for row in board2]
    expected2[1][2] = "X"
    TESTS = [
        ([r[:] for r in board], [3, 0], expected),
        ([r[:] for r in board2], [1, 2], expected2),
    ]
    passed = 0
    for b, click, exp in TESTS:
        got = sol.updateBoard(b, click)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] click={click} -> ok")
    print(f"\n{passed}/{len(TESTS)} passed")
