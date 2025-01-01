from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(s, comb: List[int]):
            if len(comb) == k:
                answer.append(comb)
                return

            for i in range(s + 1, n + 1):
                dfs(i, comb + [i])

        for i in range(1, n + 1):
            dfs(i, [i])

        return answer

answer = Solution().combine(4, 2)
print("answer", answer)
