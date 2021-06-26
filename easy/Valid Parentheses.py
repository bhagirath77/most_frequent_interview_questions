# question link : https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        di={"(":")","[":"]","{":"}"}

        for char in s:
            if char in di:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if di[stack.pop()]!=char:
                    return False
                
        return len(stack)==0
