class Solution:
    def trap(self, height: List[int]) -> int:
        # Goal is to find any empty space between two points.
        # What's interesting is that the walls occupy the container space.
        # Another 2-ptr problem.

        # Example 1:
        # <-|0, 2, 0, 3, 1, 0, 1, 3, 2, 1|->
        
        # in this example, we need to traverse the heights sequentially and consider the
        # floor of what's to the left and right, then subtract our height.

        # at h[0]: leftWall is 0, right is 2, height is 0 :. 0
        # at h[1]: leftWall is 0, right is 3, height is 2 :. 0-2 => 0
        # at h[2]: leftWall is 2, right is 3, height is 0 :. 2-0 => 2
        # at h[3]: leftWall is 2, right is 3 @ h[7], height is 3 :. 2-3 => 0
        # at h[4]: leftWall is 3, right is 3 @ h[7], height is 1 :. 3-1 => 2
        # at h[5] => 3; at h[6] => 2; at h[7] => 0, 8 => 0, 9 = 0

        if not height: return 0

        volume = 0

        # approach 2: using 2 pointers
        # why this works: 
        #   1. We know out of bounds and the outer positions cannot contain water
        #   2. By tracking the highest Left and right we've seen, we can improve
        #      approach 1 by applying max_left and max_right after applying the math.

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]

        while left < right:
            # we cannot use the max height for the current pass, but we can save it for later
            # condition 1: if max_left == max_right, we shift left +1
            # condition 2: if max_left < max_right, we shift left +1
            # condition 3: if max_right < max_left, we shift right -1
            if max_left < max_right:
                left += 1
                # because we're updating max_left before results, we guarantee non-negative results
                max_left = max(max_left, height[left])
                volume += max_left - height[left]
            else:
                right -= 1
                # same with max_right, cannot be negative
                max_right = max(max_right, height[right])
                volume += max_right - height[right]

        return volume

            

        # approach 1: pre-calculate everything
        maxLeftArr, maxRightArr = [], []
        maxLeft, maxRigt = 0, 0
        for i in range(len(height) - 1):
            curHeight = height[i]

            maxLeftArr[i] = maxLeft
            if curHeight > maxLeft:
                maxLeft = curHeight

        for i in range(len(height) - 1, 0, -1):
            curHeight = height[i]

            maxRightArr[i] = maxRight
            if curHeight > maxRight:
                maxRight = curHeight

        for i in range(len(height) - 1):
            if (min(maxLeftArr[i], maxRightArr[i]) - height[i] > 0):
                volume += height[i]


        return volume
        