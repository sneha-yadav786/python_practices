class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans=0
        idx=0
        while nums!=sorted(nums):
            m=float("inf")
            for i in range(len(nums)-1,0,-1):
                s=nums[i]+nums[i-1]
                if s<=m:
                    m=s
                    idx=i
            nums[idx]=m
            nums.pop(idx-1)
            ans+=1
        return ans
# Simple solution becaause len(arr)<=50 T.C.=O(n^2) 