# 1700. Number of Students Unable to Eat Lunch
# link : https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        myCounter = Counter(students)

        for sandwich in sandwiches:
            if myCounter[sandwich] == 0:
                break
            else:
                myCounter[sandwich] -= 1
                
        return myCounter.total()
    