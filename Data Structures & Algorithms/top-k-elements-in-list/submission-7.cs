public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // Here we need a heap to be able to pull the most frequently occuring
        // Option 1: Using Linq... [Freq, Value].GroupBy(Freq).OrderBy(Freq).Select...

        // But PriorityQueue is the more appropriate kind.

        var maxHeap = new PriorityQueue<int, int>(
            Comparer<int>.Create((a, b) => b.CompareTo(a)));

        // Populate frequency map
        int min = Math.Min(nums.Length, 2001);
        var freqMap = new Dictionary<int, int>(min); // exploit the bounds
        foreach (var num in nums)
        {
            freqMap[num] = freqMap.GetValueOrDefault(num) + 1;
        }

        foreach (var (key, value) in freqMap)
        {
            maxHeap.Enqueue(key, value);
        }

        var result = new int[k];
        for (var index = 0; index < k; index++)
        {
            result[index] = maxHeap.Dequeue();
        }

        return result;
    }
}
