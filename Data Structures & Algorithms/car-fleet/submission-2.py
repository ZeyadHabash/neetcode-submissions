class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate t for each car where t is the time it would arrive at target if it maintains the current speed
        # t[i] = (target - position[i]) / speed[i]
        # for each car i check if t[i] <= any car that has larger position[i]
        # if so these cars join fleets
        # this joining of fleets can be handled in a stack if we loop over the arrays in descending sorted order
        # we check t against the top of the stack, if t <= top, that's one fleet, dont push
        # if t > top, form a new fleet, push t onto the stack
        # at the end we can count the number of elements in the stack and thats the number of fleets
        
        # my issue here rn is how to sort both speed and position according to position's order
        sortedList = sorted(zip(position,speed), reverse=True)

        carfleet_stack = []

        for p,s in sortedList:
            time = (target - p) / s
            if (not carfleet_stack) or carfleet_stack[-1] < time:
                carfleet_stack.append(time)
        
        return len(carfleet_stack)
