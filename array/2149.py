class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        arr=[]
        arr2=[]
        for num in nums:
            if num<0:
                arr.append(num)
            else:
                arr2.append(num)
        
    

        t=1
        for i in range(0,len(arr2)):
            u=arr[i]
            j=i+t
            arr2.insert(j,u)
            t+=1
        return arr2
        

        
