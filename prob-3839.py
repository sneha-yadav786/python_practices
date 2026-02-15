from collections import defaultdict
class Solution:
    def prefixConnected(self, words, k: int) -> int:
        prefix_count=defaultdict(int)
        for word in words:
            if len(word)>=k:
                prefix=word[:k]
                prefix_count[prefix]+=1
        groups=0
        for count in prefix_count.values():
            if count>=2:
                groups+=1
        return groups