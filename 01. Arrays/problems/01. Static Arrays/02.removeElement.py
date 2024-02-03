# 27. Remove Element
# link : https://leetcode.com/problems/remove-element/description/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[left] = nums[i]
                left += 1
        return left


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
