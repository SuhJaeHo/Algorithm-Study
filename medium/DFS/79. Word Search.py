from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, visited, x, y, currIdx):
            visited[x][y] = True

            if currIdx == len(word) - 1:
                return True

            nx = [1, 0, -1, 0]
            ny = [0, 1, 0, -1]

            for i in range(4):
                dx = x + nx[i]
                dy = y + ny[i]
                if dx >= 0 and dx < len(board) and dy >= 0 and dy < len(board[0]) and board[dx][dy] == word[currIdx + 1] and not visited[dx][dy]:
                    if dfs(board, visited, dx, dy, currIdx + 1):
                        return True

            visited[x][y] = False

        visited = [[False] * len(board[0]) for _ in range(len(board))]

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if dfs(board, visited, x, y, 0):
                        return True

        return False

# answer = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
# answer = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
# answer = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
answer = Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
# answer = Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
print("answer", answer)
