class Solution:
    def merge(self, intervals) :
        intervals.sort()
        temp=[intervals[0]]
        for i in range(1,len(intervals)):
            if temp[-1][0]<=intervals[i][0]<=temp[-1][1]:
                temp[-1]=[temp[-1][0],max(temp[-1][1],intervals[i][1])]
            else:
                temp.append(intervals[i])
        return temp