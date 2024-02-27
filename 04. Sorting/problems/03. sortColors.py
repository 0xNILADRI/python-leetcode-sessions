# 75. Sort Colors
# link : https://leetcode.com/problems/sort-colors/description/

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counts = [0,0,0]
        for i in nums:
            counts[i] +=  1
        
        cont = 0

        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[cont] = i
                cont += 1

        