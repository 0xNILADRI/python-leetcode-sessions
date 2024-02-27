# 70. Climbing Stairs
# link : https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 2):
            return n
        step_arr = [1,2]
        for i in range(2, n+1):
            step_arr.append(step_arr[i-1] + step_arr[i-2])
        return step_arr[-2]