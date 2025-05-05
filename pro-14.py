class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        if len(strs)==1:
            return strs[0]
        else:
            p=""
            mini=strs[0]
            for item in strs:
               if len(item)<len(mini):
                  mini=item
            for i in range(len(mini)):
               n=False
               for k in strs:
                    if mini[i] in k and k.index(mini[i])==i:
                      n=True
                    else:
                      n=False
                      return p
               if n is True :
                   p+=mini[i]    
            return  p