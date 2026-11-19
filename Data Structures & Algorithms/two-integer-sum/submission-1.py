class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Notes: It's always 2 numbers exactly, 1 solution exactly
        # using maps
        inventory = {} # val : index

        # O(nk) --> O(n), leverage Target to spot diff early
        # where N is iterating through the container, and K is a O(1) lookup for each value
        for index, val in enumerate(nums):
            diff = target - val
            diffIndex = inventory.get(diff, 0)
            if (diffIndex != 0):
                return [diffIndex, index]
            inventory[val] = index
        

        # O(n^2), brute forcing all combinations
        for indexI, valueI in enumerate(nums):
            for indexJ in range(indexI + 1, len(nums)):
                if valueI + nums[indexJ] == target:
                    return [indexI, indexJ]