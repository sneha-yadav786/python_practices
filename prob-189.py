class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n # for handling large inputs
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]
# T.C.= O(n)
# S.C.= O(n)   