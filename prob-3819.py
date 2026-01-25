class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        temp=[x for x in nums if x>=0]
        
        if not temp:
            return nums
        k%=len(temp)
        temp=temp[k:]+temp[:k]
        j=0 
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=temp[j]
                j+=1
        return nums