# 20. Valid Parentheses
# link : https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rules = {")": "(", "}": "{", "]": "["}

        for sign in s:
            if sign in rules:
                if stack and stack[-1] == rules[sign]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sign)

        return True if not stack else False


print(Solution().isValid("()[]"))
