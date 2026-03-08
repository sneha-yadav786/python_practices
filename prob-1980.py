class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        temp=["0"]*n
        start=2**(n-1)
        end=(2**n)
        for item in range(start,end):
            if ''.join(temp) not in nums:
                return ''.join(temp)
            if bin(item)[2::] not in nums:
                return bin(item)[2::]
            