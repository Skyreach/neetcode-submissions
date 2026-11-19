class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for item in nums:
            if item in map:
                return True
            map.add(item)
        return False
        