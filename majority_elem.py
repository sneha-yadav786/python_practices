class Solution:
    def majorityElement(self, nums) :
        # using boyer-moore majority algo
        maj=nums[0]
        c=0
        for i in nums:
            if c==0:
                maj=i
                c=1
            elif maj==i:
                c+=1
            else:
                c-=1
        return maj