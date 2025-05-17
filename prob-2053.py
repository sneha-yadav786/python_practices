class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=""
        l=[]
        freq=Counter(arr)
        for i in freq:
             if freq.get(i)==1:
                s+=1
                if s==k:
                    return i
        
        return c

