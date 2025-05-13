class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        from collections import deque
        mod=10**9+7
        l=[0]*26
        for ch in s:
            l[ord(ch)-97]+=1
        l=deque(l)
        for i in range(t):
            m=l.pop() 
            l.appendleft(m)
            l[1]+=m
        return sum(l)%mod


