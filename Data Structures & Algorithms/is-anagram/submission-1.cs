public class Solution {
    public bool IsAnagram(string s, string t) {
        // Approach 1: Carry 2 maps w/ counts by key
        // CompareWithMaps(s, t);

        // Approach 2: Chacater Hashes
        var counts = new int[26];
        foreach (var ch in s)
        {
            counts[ch - 'a']++;
        }

        foreach (var ch in t)
        {
            counts[ch - 'a']--;
        }

        return counts.All(x => x == 0);
    }

    public bool CompareWitMaps(string s, string t)
    {
        var sCharMap = new Dictionary<char, int>();
        var tCharMap = new Dictionary<char, int>();

        if (s.Length != t.Length) return false;

        foreach (var ch in s)
        {
            sCharMap[ch] = sCharMap.ContainsKey(ch) ?
                sCharMap[ch] + 1 :
                1;
        }

        foreach (var ch in t)
        {
            tCharMap[ch] = tCharMap.ContainsKey(ch) ?
                tCharMap[ch] + 1 :
                1;
        }

        foreach (var key in sCharMap.Keys) 
        {
            if (!tCharMap.ContainsKey(key))
            {
                return false;
            }

            if (tCharMap[key] != sCharMap[key]) 
            {
                return false;
            }
        }
        
        return true;
    }
}
