public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // We're trying to group all "anagrams" into a bucket-list
        // Initial thought was to use hashes but this hits potential collisions...
        // Instead, let's use the Anagram array as our key.

        var container = new Dictionary<string, List<string>>(strs.Length);
        foreach (var str in strs)
        {
            var keyArray = new int[26];
            foreach (var ch in str)
            {
                keyArray[ch - 'a']++;
            }
            var key = string.Join(',', keyArray);
            if (!container.TryGetValue(key, out var list))
            {
                list = new List<string>();
                container[key] = list;
            }
            list.Add(str);
        }

        return container.Values.ToList();
    }
}
