# 1929. Concatenation of Array
# link : https://leetcode.com/problems/concatenation-of-array/description/


from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for n in nums:
                ans.append(n)
        return ans


print(Solution().getConcatenation([1, 3, 2, 1]))
