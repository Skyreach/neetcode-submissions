public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        // [] solutions
        // req's knowing values at each position other than itself
        // As we need O(n), we need to look at the container
        // prefixProduct | index | suffixProduct
    
        // To do O(n) we'd need to do it all in one pass...
        // We can achieve this by calculating the prefixes and suffixes in one pass.
        /*
        Example input: [1, 2, 3, 4]
        prefixes: [1, 2, 6, 24] // O(n)
        suffixes: [24, 24, 12, 4] // O(n)

        Once we have this, we can iterate through the container, and multiply the appropriate prefix/suffix
        Note: oob's (i.e. prefixes @ -1 and suffixes @ Length + 1 are 1 to be inert)
        */

        var output = new int[nums.Length];
        // var prefixes = new int[nums.Length];
        // var suffixes = new int[nums.Length];
        // could combine them and use the output container instead

        var prefix = 1;
        for (var index = 0; index < nums.Length; index++)
        {
            // load prefix
            output[index] = prefix;
            prefix *= nums[index];
        }

        var suffix = 1;
        for (var index = nums.Length - 1; index >= 0; index--)
        {
            // load suffix
            output[index] *= suffix;
            suffix *= nums[index];
        }

        return output;
    }
}
