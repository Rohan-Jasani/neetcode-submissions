class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [ (target - pos)/v for pos, v in zip( position, speed ) ]
        cars = sorted( list( zip( position, time ) ), reverse = True )
        # print( cars )
        max_t = 0
        fleets = 0
        for pos, t in cars:
            if t > max_t: 
                fleets += 1
                max_t = t
        return fleets
        

        
