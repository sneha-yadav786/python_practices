class Solution:
    def merge(self, nums1, m, nums2, n):
        idx=len(nums1)-1
        i=m-1 # phli list ka maximum element
        j=n-1 # doosri list ka maximum element
        # nums1 me piche se maximum element insert krte jao..
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[idx]=nums2[j]
                j-=1
            else:
                nums1[idx]=nums1[i]
                i-=1
            idx-=1
        while j>=0:
            nums1[idx]=nums2[j]
            j-=1
            idx-=1