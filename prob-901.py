class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        stack=self.stack
        count=1
        while stack and stack[-1][0]<=price:
            count+=stack[-1][1]
            stack.pop()
        stack.append([price,count])
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)