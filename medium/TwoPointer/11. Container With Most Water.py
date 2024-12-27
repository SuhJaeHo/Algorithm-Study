from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0

        # 더 낮은 높이 인덱스 한칸씩 조정
        l = 0
        r = len(height) - 1

        while l != r:
            if height[r] >= height[l]:
                answer = max(height[l] * (r - l), answer)
                l += 1
            else:
                answer = max(height[r] * (r - l), answer)
                r -= 1

        return answer

answer = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print("answer", answer)
