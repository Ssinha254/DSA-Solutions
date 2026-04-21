# Last updated: 4/21/2026, 11:25:26 PM
class Solution(object):    
    def readBinaryWatch(self, turnedOn):
        def no_of_bits(n):            
            count = 0           
            while n != 0:                 
                if n % 2== 1:                     
                    count += 1                 
                n = n // 2             
            return count        
        res = []         
        for hour in range(0, 12):            
            for minute in range(0,60):                 
                bits = no_of_bits(hour) + no_of_bits(minute)                 
                if bits == turnedOn:                     
                    res.append(f"{hour}:{minute:02d}")         
        return res