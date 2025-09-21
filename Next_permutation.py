class Solution(object):
    def nextPermutation(self, nums):
        idx=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx==-1:
            nums.reverse()
        else:
            for j in range(len(nums)-1,idx,-1):
                if nums[j]>nums[idx]:
                    nums[idx],nums[j]=nums[j],nums[idx]
                    break
        
            nums[idx+1:]=reversed(nums[idx+1:])
        #isse bhi better approch use kr skte h using while loop in place of for loop and if statement.