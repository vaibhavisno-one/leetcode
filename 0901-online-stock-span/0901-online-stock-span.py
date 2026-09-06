class StockSpanner:

    def __init__(self):
        self.st=[]
        
        

    def next(self, price: int) -> int:

        s=1
        while self.st and self.st[-1][0]<=price:
            s+=self.st.pop()[-1]
        self.st.append([price,s])

        return s
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)