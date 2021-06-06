# Question link: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: int) -> List[int]:
        l=[0]
        for i in range(1,num+1):
            if(i%4==1):
                l.append(l[-1]+1)
            elif(i%4==2):
                l.append(l[-1])
            elif(i%4==3):
                l.append(l[-1]+1)
            else:
                
                c=0
                while i:
                    c+=1
                    i&=(i-1)
                l.append(c)
        return l
        
