#question link: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        curr = 1
        for i in range(len(nums) - 2, -1, -1):
            curr *= nums[i + 1]
            ans[i] *= curr
        return ans
