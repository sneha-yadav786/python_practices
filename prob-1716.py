class Solution:
    def totalMoney(self, n: int) -> int:
        r=(n//7)+1
        ans=0
        round=0
        while round<r:
            if n>=7:
                m=7
            else:
                m=n
            n-=m
            for i in range(1,m+1):
                ans+=(i+round)

            round+=1
        return ans