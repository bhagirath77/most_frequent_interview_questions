#question link : https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        d=set()
        for a,b in c.most_common(k):
            d.add(a)
        return d
        
