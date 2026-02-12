class Solution:
    def longestBalanced(self, s: str) -> int:
        ans=0
        n=len(s)
        for i in range(n):
            freq=[0]*26 #[0,0,0,0,0,0,........](26 size)
            max_freq=0
            unique=0
            for j in range(i,n):
                idx=ord(s[j])-ord('a')
                if freq[idx]==0:
                    unique+=1# count unique element when it comes first time
                freq[idx]+=1
                max_freq=max(max_freq,freq[idx])
                if max_freq*unique==j-i+1:# Note
                    ans=max(ans,j-i+1)
        return ans