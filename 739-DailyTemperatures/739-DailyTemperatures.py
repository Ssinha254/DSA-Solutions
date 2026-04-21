# Last updated: 4/21/2026, 11:24:58 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(temperatures)
        i = 0
        stack =[]
        while i <len(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top =stack.pop()
                answer[top] = i - top
            stack.append(i)
            i+=1
        return answer

