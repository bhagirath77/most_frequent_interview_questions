# question link : https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        x=[]
        def para(s,y,z):
            if y==0 and z==n:
                x.append(s)
                return
            if z<n:
                para(s+"(",y+1,z+1)
            if y>0:
                para(s+")",y-1,z)
        para("",0,0)
        return x
