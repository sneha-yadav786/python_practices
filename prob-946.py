class Solution:
    def validateStackSequences(self, pushed,popped):
        idx=0
        stack=[]
        for i in pushed:
            stack.append(i)
            while stack and idx<len(popped) and popped[idx]==stack[-1]:
                stack.pop()
                idx+=1
        if not stack:
            return True
        else:
            return False


        