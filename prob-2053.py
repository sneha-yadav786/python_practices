class Solution:
    def kthDistinct(self, arr, k):
        c=""
        s=0
        l=[]
        freq=Counter(arr)
        for i in freq:
            if freq.get(i)==1:
                s+=1
                if s==k:
                    return i
        
        return c
