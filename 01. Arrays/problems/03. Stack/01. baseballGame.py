# 682. Baseball Game
# link : https://leetcode.com/problems/baseball-game/description/

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        res = 0
        for item in operations:
            if item == "C":
                ans.pop()
            elif item == "D":
                ans.append(int(ans[-1]) * 2)
            elif item == "+":
                ans.append(int(ans[-1]) + int(ans[-2]))
            else:
                ans.append(item)
        for i in ans:
            res += int(i)

        return res


print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
