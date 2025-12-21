"""Instead of thinking:

Which characters should I delete?

Think:

Which character should I keep?

If you decide to keep character 'x', then:

You must delete all other characters"""
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        Totalcost=0  #sum of cost array 
        ans=float("inf")
        mp={}
        for i in range(len(s)):
            # we add all costs respectively perticular chr
            if s[i] in mp:
                mp[s[i]]+=cost[i]
            else:
                mp[s[i]]=cost[i]
            Totalcost+=cost[i]
        for i in mp:
            # find min of totalcost-present element cost
            ans=min(ans,Totalcost-mp[i])
        return ans
        
