class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        r1=version1.split(".")
        r2=version2.split(".")
        m=abs(len(r1)-len(r2))
        if len(r1)<len(r2):
            for j in range(m):
                r1.append('0')
        else:
            for j in range(m):
                r2.append('0')
        for i in range(len(r1)):
            if int(r1[i]) > int(r2[i]):
                return 1
            elif int(r2[i]) > int(r1[i]):
                return -1
        return 0
