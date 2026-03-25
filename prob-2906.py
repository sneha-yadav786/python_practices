class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod=12345
        n=len(grid)
        m=len(grid[0])
        f=[[0]* m for _ in range(n)]
        s=1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                f[i][j]=s
                s=(s*grid[i][j])%mod
        p=1
        for i in range(n):
            for j in range(m):
                f[i][j]=(f[i][j]*p)%mod
                p=(p*grid[i][j])%mod
        return f
