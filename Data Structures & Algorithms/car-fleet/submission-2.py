class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        class Car:
            def __init__(self, position, speed):
                self.position = position
                self.speed = speed
                self.hours = (target - position) / speed

        cars = []
        for i, pos in enumerate(position):
            cars.append( Car(position=pos, speed=speed[i]) )
        
        cars.sort(key=lambda x: x.position)

        for i in reversed(range(len(cars)-1)):
            if cars[i].hours < cars[i+1].hours:
                cars[i].hours = cars[i+1].hours
        
        total = 0

        while cars:
            curr = cars.pop()
            while cars and cars[-1].hours == curr.hours:
                cars.pop()
            total += 1

        return total