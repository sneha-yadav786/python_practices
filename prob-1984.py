class Solution:
    def minimumDifference(self, nums, k):
        ans=(10**5)+1
        nums.sort()
        i,j=0,k-1
        while i<len(nums) and j<len(nums):
            m=nums[j]-nums[i]
            ans=min(m,ans)
            i+=1
            j=i+k-1
        return ans