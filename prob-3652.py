class Solution:
    def maxProfit(self, prices, strategy, k):
        Total_Profit=0
        max_gain=0
        profit=[0]*len(prices)
        for i in range(len(prices)):
            profit[i]=prices[i]*strategy[i]
            Total_Profit+=profit[i]
        max_sum,org_sum=0,0
        i=0
        for j in range(len(prices)):
            org_sum+= profit[j]
            if j-i+1>k//2:# jab adhi se jyada window ho jaye to direct jod do
                max_sum+= prices[j]
            if j-i+1>k:#window size>k means time to shrink
                org_sum-= profit[i]
                max_sum-= prices[i+(k//2)]
                i+=1
            if j-i+1==k:#exact window obtained update the ans
                max_gain=max(max_gain,max_sum-org_sum)
        return Total_Profit+max_gain

