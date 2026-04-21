# Last updated: 4/21/2026, 11:25:25 PM
from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = deque()  # Stack to store digits

        for i in num:
            i = int(i)

            # Remove larger digits when a smaller one is encountered
            while k and stk and i < stk[-1]:
                stk.pop()
                k -= 1
            
            stk.append(i)

        # If k is still greater than 0, remove from the back
        while k and stk:
            stk.pop()
            k -= 1

        # Remove leading zeros
        while stk and stk[0] == 0:
            stk.popleft()

        # Convert to string and return "0" if empty
        return ''.join(map(str, stk)) if stk else "0"
