class Solution:
    def minimize(self,row,col,arr):
        #for right guarded count
        for i in range(col+1,len(arr[0])):
            if arr[row][i]==2 or arr[row][i]==3:
                break
            arr[row][i]=1
        #for left guarded count
        for i in range(col-1,-1,-1):
            if arr[row][i]==2 or arr[row][i]==3:
                break
            arr[row][i]=1
        # for up guarded count
        for i in range(row-1,-1,-1):
            if arr[i][col]==2 or arr[i][col]==3:
                break
            arr[i][col]=1
        # for down guarded count
        for i in range(row+1,len(arr)):
            if arr[i][col]==2 or arr[i][col]==3:
                break
            arr[i][col]=1
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        temp=[[0 for _ in range(n)] for _ in range(m)]
        for i in guards:# 2 for guards in matrix
            p=i[0]
            q=i[1]
            temp[p][q]=2
        for j in walls:# 3 for walls in matrix
            p=j[0]
            q=j[1]
            temp[p][q]=3
        for i in guards:
            p=i[0]
            q=i[1]
            self.minimize(p,q,temp)
        count=0
        for i in range(m):
            for j in range(n):
                if temp[i][j]==0:
                    count+=1
        return count

        