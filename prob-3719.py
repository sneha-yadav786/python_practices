class Solution:
    def longestBalanced(self, nums):  
        ans=0
        n=len(nums)
        for i in range(n):
            seen=set()
            c=[0,0]# 0th index for count the even numbers and 1th index for count the odd numbers.
            # It is better way to count the occurance of elements.
            for j in range(i,n):
                if  nums[j] not  in seen:
                    seen.add(nums[j])
                    # Add unique elements in set
                    c[nums[j]%2]+=1
                if c[0]==c[1]:
                    ans=max(ans,j-i+1)
        return ans
