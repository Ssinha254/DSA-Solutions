# Last updated: 4/21/2026, 11:25:05 PM
from collections import deque
class Solution(object):
    def asteroidCollision(self,asteroids):
        stk = deque()
        for asteroid in asteroids:
            while stk and asteroid < 0 < stk[-1]:
                if abs(asteroid) > abs(stk[-1]):
                    stk.pop()  # Top is destroyed; continue to compare asteroid
                    continue
                elif abs(asteroid) == abs(stk[-1]):
                    stk.pop()  # Both destroyed
                break  # asteroid is destroyed, or equal, exit loop
            else:
                stk.append(asteroid)
        return list(stk)