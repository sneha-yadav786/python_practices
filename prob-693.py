class Solution:
    def hasAlternatingBits(self, n) -> bool:
        n=bin(n)
        temp=str(n[2::])
        for i in range(1,len(temp)):
            if temp[i]==temp[i-1]:
                return False
        return True

        