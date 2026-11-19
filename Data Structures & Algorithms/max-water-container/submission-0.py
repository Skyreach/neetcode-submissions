class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Example 1
        # <-| 1, 7, 2, 5, 4, 7, 3, 6 |->
        #      1, 5, 8, 12, 28, 18, *36* 
        # things to consider: 
        # - Height of the Left Wall
        # - Run between Left and Right
        # - Height of the Right Wall
        # Goal: Have the highest product, of min (left, right) * run

        # Example 2
        # <-| 2, 2, 2 |->
        #      2, 4

        max_volume = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            run = right - left
            current_volume = min(heights[left], heights[right]) * run
            if (max_volume < current_volume):
                max_volume = current_volume
                continue

            # because we're interested in the max area (and not an integral)
            # we only want to move 1 wall at a time. Which wall? The smaller one.
            # We're hoping that we gain more height than what we lose in run.
            # Note! If the walls are equal height we need to move one.
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1


        
        return max_volume


