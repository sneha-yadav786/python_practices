class Solution:
    def lexSmallest(self, s: str) -> str:
        l=[s]
        for i in range(1,len(s)):
            s1=s[i::-1]+s[i+1::]
            l.append(s1)
        for i in range(-1,-len(s)-1,-1):
            s1=s[:len(s)+i:]+s[-1:i-1:-1]
            l.append(s1)
        return min (l)
