# question link : https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x=nums[0]
        macs=nums[0]
        for i in range(1,len(nums)):
            macs=max(macs+nums[i],nums[i])
            if macs>x:
                x=macs
        return x
