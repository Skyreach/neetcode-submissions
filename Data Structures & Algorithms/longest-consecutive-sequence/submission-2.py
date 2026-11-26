class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We can populate a set efficiently:
        numbers_seen = set(nums)

        # I believe the solution is simply to iterate through each item of nums
        # if num - 1 in numbers_seen, we skip
        # else we would see how far the chain goes

        largest_sequence = 0
        for num in nums:
            if num - 1 in numbers_seen:
                continue

            run = 0
            while num + run in numbers_seen:
                run += 1

            largest_sequence = max(largest_sequence, run)

        return largest_sequence