class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            n=[]
            for  i in range(len(nums)-1):
                n.append((nums[i]+nums[i+1])%10)
            nums=n
            return self.triangularSum(nums)
        