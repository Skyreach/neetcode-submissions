class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Simple application of a set, add the item to a container if set contains num return true!

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        