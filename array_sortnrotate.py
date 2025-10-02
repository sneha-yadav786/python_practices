class Solution:
    def check(self, nums: List[int]) -> bool:
        s=[]
        for i in nums:
            s.append(i)
        s.sort()
        s=s[::-1]
        for i in range(len(s)):
            
            if s[:i][::-1]+s[i:][::-1]==nums:

                return True
        return False    
