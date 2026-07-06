class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        stack = []

        for pos, spd in sorted(zip(position, speed), reverse = True):
            time = (target - pos) / spd 

            if not stack:
                fleets += 1
                stack.append(time)

            if stack and stack[-1] < time:
                stack.append(time)
                fleets += 1
            
        return fleets
