class Solution:
    def validcode(self,s):
        if len(s)<1:
            return False
        valid="1234567890_"
        for i in s:
            if not i.isalpha() and i not in valid:
                return False
        return True

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans=[]
        final_ans=[]
        valid=["electronics","grocery","pharmacy","restaurant"]
        for i in range(len(isActive)):
            if isActive[i]:
                if self.validcode(code[i]) and businessLine[i] in valid:
                    ans.append([businessLine[i],code[i]])
        b=(sorted(ans, key=lambda x:(x[0],x[1])))
        for i in b:
            final_ans.append(i[1])
        return final_ans



        