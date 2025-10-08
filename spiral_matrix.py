class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        left,top=0,0
        right,bottom=len(matrix[0])-1,len(matrix)-1
        while len(ans)<len(matrix)*len(matrix[0]):
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    ans.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    ans.append(matrix[l][left])
                left+=1
        return ans
