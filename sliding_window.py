from collections import Counter
class Solution:
    def minWindow(self, s, p):
        if not s or not p:
            return ""
        countP=Counter(p)
        h={}
        have,need=0,len(countP)
        res=[-1,-1]
        resLen=float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            h[c]=h.get(c,0)+1
            if c in countP and h[c]==countP[c]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                h[s[l]]-=1
                if s[l] in countP and h[s[l]]<countP[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float("inf") else ""
        
        