class Solution:
    def minimumDistance(self, nums):
        if len(nums)<3:
            return -1
        ans=float("inf")
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    for k in range(j+1,n):
                        if nums[k]==nums[j]:
                            ans=min(ans,2*(k-i))
        if ans==float("inf"):
            return -1
        else:
            return ans