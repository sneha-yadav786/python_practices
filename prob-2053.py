class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=""
        l=[]
        freq=Counter(arr)
        for i in freq:
<<<<<<< HEAD
             if freq.get(i)==1:
=======
            if freq.get(i)==1:
>>>>>>> f14b8b9 (Added solution 165)
                s+=1
                if s==k:
                    return i
        
        return c
<<<<<<< HEAD

=======
>>>>>>> f14b8b9 (Added solution 165)
