class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        r1,r2=[],[]
        for i in version1:# jha jha '.' mil rha vha tk ki string ko int le form me ek list me store krrhe.
            if i==".":
                r1.append(int(version1[:version1.index(i):]))
                version1=version1[version1.index(i)+1::]
        r1.append(int(version1)) # . ke baad vala part add krrhe ex-12.34.56.9 to 56 tk to add ho jayega 9 ko add krrhe ab.

        for j in version2:
            if j==".":
                r2.append(int(version2[:version2.index(j):]))
                version2=version2[version2.index(j)+1::]
        r2.append(int(version2))
        l=abs(len(r1)-len(r2))
        if len(r1)>len(r2):# jo choti len ki list hogi usme utne hi zero add krdo kyuki compare krna h to element equal hone chahiye.
            for i in range(l):
                r2.append(0)
        else:
            for i in range(l):
                r1.append(0)


        for i in range(len(r1)):
            if  r1[i]>r2[i]:
                return 1
            if r2[i]>r1[i]:
                return -1
        return 0
