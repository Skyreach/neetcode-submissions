class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if we ignoreed the O(1) storage constraint, we could use a set
        # then leverage the target value to see if we'd previously discovered the value

        # instead, we need to take advantage of the fact that the container is already sorted.

        # while we can assume a solution exists, we also know that not every value has a solution
        # Because we cannot use additional containers, we need to iterate through what we have
        # Their example masks the solution... If instead we had
        # numbers = [1, 3, 4, 5, 7, 10, 11], target = 9; this would make it much more clear

        # Let's assume we can find the solution by traversing the container, taking advantage of it being sorted
        # 1 doesn't have a match, at 1+10 it's impossible to it the target; so we can ignore anything right of 10
        left, right = 0, len(numbers) -1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                left += 1
            else:
                right -= 1