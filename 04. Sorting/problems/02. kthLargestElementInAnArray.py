# 215. Kth Largest Element in an Array
# link : https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSort(nums):
            if len(nums) <= 1:
                return nums

            pivot = nums[len(nums)//2]

            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]

            return quickSort(left) + middle + quickSort(right)

        nums = quickSort(nums)
        return nums[-k]