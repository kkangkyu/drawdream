class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mapp = {")": "(", "}": "{", "]": "["} # disctonary

        for char in s:
            if char in mapp:
                a = stack.pop() if stack else 'x'
                if mapp[char] != a:
                    return False
            else:
                stack.append(char)

        return not stack


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
