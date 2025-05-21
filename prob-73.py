class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        sub_len=len(matrix[0])
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    l.append(i)
                    l.append(j)
        for i in range(0,len(l),2):
            first=l[i]
            second=l[i+1]
            print(first,second)
            matrix[first]=[0]*sub_len
            for h in range(len(matrix)):
                matrix[h][second]=0