class Solution:
    def smallestNumber(self, n: int) -> int:
        #bacause set bits are=1,3,7,15,31,63,127...(2 ki power ka no.-1)
        result=1
        while result<n:
            result=(2*result)+1
        return result