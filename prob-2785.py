class Solution:
    def sortVowels(self, s: str) -> str:
        temp="AEIOUaeiou"
        e=[]
        t=""
        for i in s:
            if i in temp:
                e.append(i)
        e.sort()
        h=0
        for j in s:
            if j in temp:
                t+=e[h]
                h+=1
            else:
                t+=j
        return t
                