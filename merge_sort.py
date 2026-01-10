def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def mergesort(arr):
    if len (arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)
a=[23,32,45,3,9,67,56]
print(mergesort(a))
    

