class Solution:
    def isTrionic(self, nums):
        i=0 
        while i+1<len(nums) and nums[i]<nums[i+1]:
            i+=1
        if i==0 :
            return False
        while i+1<len(nums) and nums[i]>nums[i+1]:
            i+=1
        if i==len(nums)-1:
            return False
        while i+1<len(nums) and nums[i]<nums[i+1]:
            i+=1
        return i==len(nums)-1
        