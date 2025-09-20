class Solution:
    def moveZeroes(self, nums):
        i, items=0, 0
        while i<len(nums) and items<=len(nums):
            if nums[i]==0: nums.append(0); nums.pop(i); i-=1
            i+=1; items+=1
