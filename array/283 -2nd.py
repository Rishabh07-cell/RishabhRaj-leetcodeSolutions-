class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        
        
        temp=[]
        for i in range(0,n):
            if nums[i]!=0:
                temp.append(nums[i])
        n1=len(temp)
        for i in range(0,n1):
            nums[i]=temp[i]
        for i in range(n1,n):
            nums[i]=0

 
       
        
