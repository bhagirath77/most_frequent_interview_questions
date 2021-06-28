# question link : https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        found = {}
        for num in nums:
            if num in found:
                return num
            else:
                found[num] = 1
