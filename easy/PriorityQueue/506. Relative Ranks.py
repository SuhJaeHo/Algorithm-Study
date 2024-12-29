from typing import List
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = [0] * len(score)

        hm = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }

        hq = []
        for i in range(len(score)):
            heapq.heappush(hq, [-score[i], i])

        for i in range(len(hq)):
            [_, idx] = heapq.heappop(hq)
            if i <= 2:
                answer[idx] = hm[i + 1]
            else:
                answer[idx] = str(i + 1)

        return answer

answer = Solution().findRelativeRanks([10,3,8,9,4])
print("answer", answer)
