class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        f=sum(apple)
        capacity.sort(reverse=True)
        ans=0
        m=0
        for i in capacity:
            if m<f:
                m+=i
                ans+=1
            else:
                break
        return ans
           
        