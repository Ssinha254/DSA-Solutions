# Last updated: 4/21/2026, 11:28:00 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        for i in s :
            if i =='(' or i == "{" or i == "[":
                stk.append(i)
            elif i ==")" and stk and stk[-1] == "(" :
                stk.pop()
            elif i =="}" and stk and stk[-1] == "{" :
                stk.pop()
            elif i =="]" and stk and  stk[-1] == "[" :
                stk.pop()
            else:
             return False
        return len(stk) ==0