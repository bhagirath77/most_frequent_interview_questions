class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        low = 0
        arr=[-2**31-1]+arr+[-2**31-1]
        high = len(arr) - 1
        mid = 0
        print(high)
        if(high==0):
            return 0
        if(high==1):
            return 1 if arr[-1]>arr[0] else 0
        while low <= high: 
            mid = (high + low) // 2
            if arr[mid] < arr[mid+1]: 
                low = mid + 1
            elif arr[mid] < arr[mid-1]: 
                high = mid - 1
            else: 
                return mid-1

        
