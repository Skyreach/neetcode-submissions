class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I think we can leverage a set, because set preserves order
        # and we're looking for a diff; in the container

        # incorrect! We cannot use a set because this does not preserve the index
        # use a map!

        unmatched_by_position = {}  # [value, idx]

        for index, num in enumerate(nums):
            diff = target - num
            if bool(unmatched_by_position) and diff in unmatched_by_position:
                return [unmatched_by_position[diff], index]

            unmatched_by_position[num] = index