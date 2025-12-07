class Solution:
    def odd(self,num):
        if num%2!=0:
            return True
        else:
            return False
    # the question is based on simple mathematics observation.
    def countOdds(self, low, high) :
        c=int((high-low)/2)
        if self.odd(low) or self.odd(high):
            c+=1
        return c