# Last updated: 4/21/2026, 11:26:34 PM
class MinStack:

    def __init__(self):
        self.stk = deque()
    
    def top(self) -> int:
        return self.stk[-1][0]
        

    def push(self, val: int) -> None:
        if(len(self.stk)==0):
            self.stk.append([val, val])
        else:
            self.stk.append([val, min(val, self.stk[-1][1])])
        

    def pop(self) -> None:

        return self.stk.pop()
        

    
        

    def getMin(self) -> int:
        return self.stk[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()