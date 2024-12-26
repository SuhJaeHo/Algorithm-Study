from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums.sort()
        hm = {}

        s = 0
        while s <= len(nums) - 3:
            if s > 0 and nums[s] == nums[s - 1]:
                s += 1
                continue

            l = s + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[s] + nums[l] + nums[r]
                if sum == 0:
                    key = str(nums[s]) + str(nums[l]) + str(nums[r])
                    if not hm.get(key):
                        hm[key] = True
                        answer.append([nums[s], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    continue

                if sum > 0:
                    r -= 1
                else:
                    l += 1

            s += 1

        return answer

answer = Solution().threeSum([-1,0,1,2,-1,-4])
print("answer", answer)
