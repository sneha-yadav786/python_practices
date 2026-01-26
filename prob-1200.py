class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        d={}
        for i in range(1,len(arr)):
            d[(arr[i-1],arr[i])]=arr[i]-arr[i-1]
        n=min(list(d.values()))
        ans=[]
        for i in d:
            if d[i]==n:
                ans.append(i)
        return ans

        