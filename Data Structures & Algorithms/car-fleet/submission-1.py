class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Example 1, walking through the example
        # Array 1 defines where a car is along its path; i.e. 
            # there's a car @ 1 mile
            # and another @ 4 miles
            # 1 -> 4, 4 -> 6; 4 -> 7, 6 -> 8, 7 -> 10, 8 -> 10; 
            # both arrive at the same time, 1 fleet

        # Example 2:
        # 4, 1, 0, 7; 2, 2, 1, 1 (t = 10)
        # 4 -> 6; 1 -> 3, 0 -> 1, 7 -> 8
        # 6 -> 8, 3 -> 5, 1 -> 2, 8 -> 9
        # [8 -> 10 (9 -> 10)], 5 -> 7, 2 -> 3
        # 7 -> 9, 3 -> 4

        # Thoughts, we're starting w/ N cars; each moving at a speed
        # Their position is always increasing
        # As cars cannot pass, we need to determine when a car merges with the group
        

        # NeetCode explanation:
        # Here it's easier to look at the problem based on the time required for each vehicle to
        # make it to the end. Using Example 2 (position, speed):
        # [(4,2), (1, 2), (0, 1), (7, 1)]
        # First, we want to sort by position -> [(0,1), (1,2), (4, 2), (7,1)]
        # Next, because Rightmost vehicles are blocking, we calculate T from Right to Left.
        # (10 - 7) / 1 = 3, (10 - 4) / 2 = 3, (10 - 1) / 2 = 5, (10 - 0) / 1 = 10
        # By inspection, we can see R1 and R2 will be 1 fleet, R3 is 1 fleet, R4 is 1 fleet.

        # 1, build the container, then sort
        stats = sorted(zip(position, speed), reverse = True)

        stack = [] # vehiclesInFleet
        for pos, speed in stats:
            t = (target - pos) / speed
            # if not stack or t > stack[-1]:
            #     stack.append(t)
            # a slower car has a higher T, ties are skipped
            if stack and stack[-1] >= t:
                continue
            stack.append(t)

        return len(stack)