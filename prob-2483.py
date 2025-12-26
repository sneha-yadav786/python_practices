class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # is question me bas itna observe krna hai ki perticular index pr penalty kis basis pr count ho rhi (penulty=number of N till i-1 + number of Y from i to last )
        count_Y=customers.count("Y")
        count_N,m=0,float("inf")
        ans=-1
        for i in range(len(customers)):
            temp=count_N #previous count of N(just ek index phle tk)
            if customers[i]=="N":
                count_N+=1
            if  count_Y+temp<m:
                m=count_Y+temp
                ans=i
            if customers[i]=="Y":
                count_Y-=1
        if count_N<m:
            m=count_N
            ans=i+1
        return ans
        