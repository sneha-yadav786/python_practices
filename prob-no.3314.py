class Solution:
    def minBitwiseArray(self, nums):
        ans=[]
        for i in nums:
            n=False
            for j in range(1,i):
                if (j | j+1)==i: # OR(logical(T/F)) aur |(bitwise) me diff hota hai 
                    ans.append(j)
                    n=True
                    break
            if not n:
                ans.append(-1)
        return ans
        