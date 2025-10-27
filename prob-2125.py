class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        a=[]
        for i in bank:
            cont=i.count('1')
            if cont>=1:
                a.append(i.count('1'))
        if len(a)<=1:
            return 0
        else:
            ans=0
            for j in range(len(a)-1):
                ans+=a[j]*a[j+1]
            return ans