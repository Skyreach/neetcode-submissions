class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [] solutions
        # req's knowing values at each position other than itself
        # We cannot simply multiply all values then divide as this likely makes / 0
        # instead, we should have prefixes and suffixes
        # this way, we can learn all things multiplied before; and multiply that by all things after

        res = [1] * len(nums)

        prefix = 1
        # consider: Going forward for prefixes; going backward for suffixes
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Note the middle -1! We didn't stop in time.
        for i in range(len(nums) - 1, - 1, - 1):
            res[i] *= suffix
            suffix *= nums[i]

        return res



