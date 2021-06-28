# question link : https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        x=0
        prev=0
        for i in nums:
            x,prev=max(prev+i,x),x
        return x
