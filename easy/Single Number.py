#question link : https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lis={}
        for i in nums:
            if i in lis:
                del lis[i]
            else:
                lis[i]=1
        for key in lis:
            return key
