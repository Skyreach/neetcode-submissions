class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the easiest way to tackle this problem is to visualize and walkthrough an example manually
        # For Example 1, let's assume it's sorted (even though we cannot sort as O(nlogn) breaks the task)
        # <--2,3,4,4,5,10,20--> As we don't care about duplicates this reduces to <--2,3,4,5,10,20-->

        # if we continue observing, we see {2,3,4,5} is the largest, and {10} and {20} are both size 1.
        # Asking the trivial question, how do we know when a sequence is done?
        # 2 is the smallest and 5 is the largest of the sequence.
        # As we're checking a step of 1, we can assume sequences break if the item isn't found
        container_as_set = set(nums)

        largest_sequence = 0
        for num in nums:
            # check if not the start of a sequence
            if num - 1 in container_as_set:
                continue

            # start of sequence found
            consecutive_count = 0
            loop_guard = len(nums)
            while num + consecutive_count in container_as_set or consecutive_count > loop_guard:
                consecutive_count += 1

            if consecutive_count > largest_sequence:
                largest_sequence = consecutive_count
            
        return largest_sequence