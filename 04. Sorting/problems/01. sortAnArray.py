# 912. Sort an Array
# link : https://leetcode.com/problems/sort-an-array/description/

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums)//2

        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        return merge(left, right)
    
    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        
        result.extend(left[left_idx:])
        result.extend(right[right_idx:])

        return result