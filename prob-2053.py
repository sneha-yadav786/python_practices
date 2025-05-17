class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=""
        l=[]
        freq=Counter(arr)
        for i in freq:
            if freq.get(i)==1:
                l.append(i)
        if len(l)>=k:
            return l[k-1]
        else:
            return c
