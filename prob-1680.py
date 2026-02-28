class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s=""
        for i in range(1,n+1):
            s+=str(bin(i))[2:]
        a=int(s,2)
        c=a%1000000007
        return c