from collections import Counter
class Solution:
    def minArrivalsToDiscard(self, arrivals, w, m):
        ans=0
        t=[]
        for i in range(len(arrivals)):
            temp=arrivals[max(0,i-w+2):i+2]
            Count=Counter(temp)
            print(Count)
            for j in Count:
                if Count[j]>m and j not in t:
                    t.append(j)
                    print(j,Count[j])
                    ans+=1
        return ans
s1=Solution()
print(s1.minArrivalsToDiscard([8,8,8,1,7,4,3,7,5,2],7,1))