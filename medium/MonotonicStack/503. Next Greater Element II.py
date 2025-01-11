from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        answer = [-1] * len(nums)

        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                answer[stack.pop()] = nums[i]
            stack.append(i)

        for num in nums:
            while stack and num > nums[stack[-1]]:
                answer[stack.pop()] = num

        return answer


answer = Solution().nextGreaterElements([1, 2, 1])
# answer = Solution().nextGreaterElements([1,2,3,4,3])
# answer = Solution().nextGreaterElements([1,2,3,4,5,6,5,4,5,1,2,3])
print("answer", answer)
