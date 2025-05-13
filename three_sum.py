class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        a=[]
        i,j=0,len(nums)-1
        while i<j:
          d=nums[i+1:j]
          b=[]
          k=0
          while k<len(d):

            if d[k] not in b:
              if nums[i]+nums[j] <-d[k]:
               k+=1
               
              elif nums[i]+nums[j] >-d[k]:
               break
               
              else:
               l=[]
               l.append(nums[i])
               l.append(nums[j])
               l.append(d[k])
               a.append(l)
               b.append(k)
               j-=1
               i=0
            else:
              i+=1
        return (a)
s1=Solution()
print(s1.threeSum([-1,-1,1,2,-2,0,4 ]))