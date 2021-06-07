#question link : https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, a: List[int]) -> List[int]:
        l=[[3000,0],[a[0],0]]
        z=[]
        for i in range(1,len(a)):
            while(l[-1][0]<a[i]):
                z.append([i-l[-1][1],l[-1][1]])
                l.pop()
            l.append([a[i],i])
        while(len(l)!=1):
            z.append([0,l[-1][1]])
            l.pop()
        z=[i[0] for i in sorted(z,key=lambda x:x[1])]
        return z 
