class Solution:
    def floydwarshall(self,adjmat,org,change,cost):
        for i in range(len(org)):
            s=ord(org[i])-97
            t=ord(change[i])-97

            adjmat[s][t]=min(adjmat[s][t],cost[i])
        # Floyd Warshall algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    adjmat[i][j]=min(adjmat[i][j],adjmat[i][k]+adjmat[k][j])

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF=float("inf")
        adj_mat=[[INF]*26 for _ in range(26)]
        a=self.floydwarshall(adj_mat,original,changed,cost) # shortest path store krega using floydwarshall algorithm
        ans=0
        for i in range(len(source)):
            if source[i]==target[i]:
                continue
            if adj_mat[ord(source[i])-97][ord(target[i])-97]==float('inf'):
                return -1
            else:
                ans+=adj_mat[ord(source[i])-97][ord(target[i])-97]
        return ans