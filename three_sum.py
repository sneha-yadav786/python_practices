from collections import Counter
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):

            # skip duplicate fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]: #YHI STEP HMARE DUPLICATES KO REMOVE KRTE HAI VRNA O(N) HAR BAAR LAGTA CHECK KRNE ME {IF ITEM IN LIST...}
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res
# BUT AISA APPROACH HUM TWO SUM VALE ME NHI USE KRENGE KYUKI YE O(N^2) HAI AUR TWO SUM KA OPTIMIZED SOLUTION O(N) ME SOLVE HOTA HAI