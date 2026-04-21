# Last updated: 4/21/2026, 11:25:58 PM
class MyQueue:

    def __init__(self):
        self.stk1 = deque()
        self.stk2 = deque()
        

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
       while self.stk1:
         self.stk2.append(self.stk1.pop())
       ele = self.stk2.pop()
       while self.stk2:
         self.stk1.append(self.stk2.pop())
       return ele

    def peek(self) -> int:
        return self.stk1[0]
        

    def empty(self) -> bool:
        return len(self.stk1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()