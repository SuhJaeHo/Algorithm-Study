from typing import List
from collections import defaultdict

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        cnt = 0

        hm = defaultdict(bool)

        def dfs(comb: List[int]):
            nonlocal cnt

            if len(comb) == n:
                cnt += 1
                if cnt == k:
                    return "".join(map(str, comb))

            for i in range(1, n + 1):
                if not hm[i]:
                    hm[i] = True
                    kth = dfs(comb + [i])
                    if kth:
                        return kth
                    hm[i] = False

        for i in range(1, n + 1):
            hm[i] = True
            kth = dfs([i])
            if kth:
                return kth
            hm[i] = False

# answer = Solution().getPermutation(3, 3)
answer = Solution().getPermutation(2, 2)
# answer = Solution().getPermutation(9, 37098)
print("answer", answer)
