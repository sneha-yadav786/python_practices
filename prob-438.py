from collections import Counter
class Solution:
    def allzero(self,count_dict):
        if all(value==0 for value in count_dict.values()):
            return True
        else:
            return False
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count=Counter(p)# make a hashmap in which frequencies are updated, when all are 0 means this is anagram.
        ans=[]
        i=0
        j=0
        while j<len(s):
            if s[j] in count:
                count[s[j]]-=1
            if j-i+1==len(p):
                if self.allzero(count):
                    ans.append(i)
                if s[i] in count:
                    count[s[i]]+=1
                i+=1
            
            j+=1
        return ans
