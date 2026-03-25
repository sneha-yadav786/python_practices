class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row=[]
        col=[]
        for rowitem in grid:
            row.append(sum(rowitem))
        for i in range(len(grid[0])):
            s=0
            for j in range(len(grid)):
                s+=grid[j][i]
            col.append(s)
        rowsum=sum(row)
        colsum=sum(col)
        r,c=0,0
        for i in range(len(row)):
            r+=row[i]
            rowsum-=row[i]
            if r==rowsum:
                return True
        for j in range(len(col)):
            c+=col[j]
            colsum-=col[j]
            if c==colsum:
                return True
        return False

            
        