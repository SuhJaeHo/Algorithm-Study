from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        def dfs(s, subset):
            answer.append(subset)

            for i in range(s, len(nums)):
                dfs(i + 1, subset + [nums[i]])

        for i in range(len(nums)):
            dfs(i + 1, [nums[i]])

        return answer

answer = Solution().subsets([1,2,3])
print("answer", answer)
