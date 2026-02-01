class Solution:
    def minimumCost(self, nums):
        mini=float("inf")
        idx=-1
        for i in range(1,len(nums)):
            if nums[i]<mini:
                mini=nums[i]
                idx=i
        sec_mini=float("inf")
        for j in range(1,len(nums)):
            if j!=idx and nums[j]<sec_mini:
                sec_mini=nums[j]
        return nums[0]+mini+sec_mini