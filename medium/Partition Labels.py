#question link: https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        print(rightmost)
        left, right = 0, 0
        result = []
        for i, letter in enumerate(S):
            right = max(right,rightmost[letter])
            if i == right:
                result += [right-left + 1]
                left = i+1
        return result
#     get last index of every element in string by making this dictionary
