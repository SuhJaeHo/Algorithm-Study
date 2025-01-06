from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        answer = 0

        hm = {}
        for num in nums:
            if hm.get(num):
                hm[num] += 1
            else:
                hm[num] = 1

        for num in nums:
            if hm.get(num + 1):
                answer = max(hm[num + 1] + hm[num], answer)
            if hm.get(num - 1):
                answer = max(hm[num - 1] + hm[num], answer)
            hm[num] -= 1

        return answer

# answer = Solution().findLHS([1,3,2,2,5,2,3,7])
# answer = Solution().findLHS([1,2,3,4])
answer = Solution().findLHS([1,1,1,1])
print("answer", answer)
