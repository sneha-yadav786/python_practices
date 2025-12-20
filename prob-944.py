class Solution:
    def minDeletionSize(self, strs):
        if len (strs)==1:
            return 0
        count=0
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if strs[i-1][j]>strs[i][j]:
                    count+=1
                    break
        return (count)
        