class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # My guess is to use 2 pointers, L, and R, and make dictionary<int, stack>
        # but this was wrong. As each container is expensive to spin up, it's better to
        # sort the container and take a nlogn hit.
        # the key note I missed is that the output should not contain any duplicate triplets. There's
        # another passive hint about the triplets being in any order, which implies sorting is okay
        # Example 1: [-1, 0, 1, 2, -1, -4]
        # Sorted [-4, -1, -1, 0, 1, 2]

        # Two Sums already tells us that we can take advantage of a sorted container with 2P
        result = []
        nums.sort()

        # iterate through using index positions
        # a, l, and r are our 3 points of interest
        for i, a in enumerate(nums):
            # a cannot repeat, skip
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    # needs guard to ensure non-dupe
                    l += 1
                else:
                    # Note: as this has more logic we make this the else, futher we want the increment here too.
                    result.append([a, nums[l], nums[r]])

                    # update pointers
                    # consider: [-2, -2, 0, 0, 2, 2]
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result