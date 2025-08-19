class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m= float('inf')
        i=0
        s=0
        for j in range(len(nums)):
            s+=nums[j]
            while s>=target:
                m=min(m,j-i+1)
                s-=nums[i]
                i+=1

                
        if m==float('inf'):
            return 0
        else:
            return m
                        
            

