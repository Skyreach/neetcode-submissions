public class Solution {
    // Notes: A hash isn't reversible; so we need a salt to split
    // There's no guarantee of which character being used.
    // Initial thought (seeing this before: Pull characters until an escape is found)
    // Limit: doesn't elimiate odds of the pattern being in the strings.
    public string Encode(IList<string> strs) {
        const string delimiter = "#";
        var composed = new List<string>();
        foreach (var str in strs)
        {
            composed.Add(str.Length.ToString());
            composed.Add(delimiter);
            composed.Add(str);
        }
        return string.Join("", composed);
    }

    public List<string> Decode(string s) {
        var result = new List<string>();
        // Assumes a valid string inputed; i.e. starts with a number
        var i = 0;
        while (i < s.Length)
        {
            // get position of delimiter
            var hash = s.IndexOf('#', i);
            var strLen = int.Parse(s.AsSpan(i, hash - i));

            result.Add(s.Substring(hash + 1, strLen));
            i = hash + 1 + strLen;
        }

        return result;
   }
}
