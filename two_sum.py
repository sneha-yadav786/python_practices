nums=[1,2,3,4,3]
nums=sorted(nums)
a,b=[],[]
target=6
i,j=0,len(nums)-1
while i<j:
  if nums[i] not in b:
    if nums[i]+nums[j]<target:
     i+=1
    elif nums[i]+nums[j]>target:
     j-=1
    else:
     l=[]
     l.append(nums[i])
     l.append(nums[j])
     a.append(l)
     b.append(nums[i])
     j-=1
     i=0
  else:
   i+=1
print(a)
