# question link : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        longest = 0
        left, right = 0, 0
        chars = set()
        while right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                while left<len(string) and string[right] in chars:
                    chars.remove(string[left])
                    left += 1
        return longest
