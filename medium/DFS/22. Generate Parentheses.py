from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def dfs(pairs, openCount, closeCount):
            if len(pairs) == n * 2:
                answer.append(pairs)
                return

            if openCount < n:
                dfs(pairs + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                dfs(pairs + ")", openCount, closeCount + 1)

        dfs("", 0, 0)

        # def dfs(pairs, n):
        #     if len(pairs) == n * 2:
        #         if n == 0:
        #             answer.append(pairs)
        #         return

        #     if n >= 1:
        #         dfs(pairs + ")", n - 1)
        #         dfs(pairs + "(", n + 1)
        #     else:
        #         dfs(pairs + "(", n + 1)

        # dfs("(", 1)

        return answer

answer = Solution().generateParenthesis(3)
print("answer", answer)
