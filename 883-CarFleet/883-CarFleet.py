# Last updated: 4/21/2026, 11:24:51 PM
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = [0]*len(position)
        for i in range(len(position)):
            cars[i] = (position[i],speed[i], (target - position[i])/float(speed[i]))

        cars = sorted(cars, reverse = True)
        print(cars)

        max_time_so_far =cars[0][2]
        fleet = 1
        for car in cars:
            if car[2] <= max_time_so_far :
                continue
            elif car[2] > max_time_so_far:
                fleet += 1
                max_time_so_far = car[2]
        return fleet