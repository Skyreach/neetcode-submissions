public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // Notes: We know there's _always_ 1 pair of indices that works
        // We can take advantage of this by using the target's diff.

        // Assume the diff is in the container; and that we're retrospecting for the correct position.

        var seen = new Dictionary<int, int>(nums.Length); // number, position
        for (var index = 0; index < nums.Length; index++)
        {
            var num = nums[index];
            var diff = target - num;
            if (seen.TryGetValue(diff, out var j))
            {
                return [j, index];
            }
            seen[num] = index;
        }

        return [];
    }
}
