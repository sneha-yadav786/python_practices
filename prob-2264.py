class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=[]
        for i in range(len(num)):
            if len(set(num[i:i+3]))==1 and len(num[i:i+3])==3:
                l.append(num[i:i+3])
        if not l:
            return ""
        else:
            maxi=l[0]
            for j in range(1,len(l)):
                if int(l[j])>=int(maxi):
                    maxi=l[j]
            
            return maxi