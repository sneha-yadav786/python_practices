class Solution:
    def missingRange(self, arr, low, high):
        result=[]
        count={}
        for i in range(low,high+1):
            count[i]=1
        for j in arr:
            count[j]=0
        for k in count:
            if count[k]==1:
                result.append(k)
        return result