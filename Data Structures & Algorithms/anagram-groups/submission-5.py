import math
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # forgot about collections
        # we want an initializer here because checking each list for empty before appending is work
        # defaultdict is probably the right play
        res = collections.defaultdict(list)

        for string in strs:
            # leverage our anagram strat.
            key = [0] * 26
            for character in string:
                relative_ord = ord(character) - ord('a')
                key[relative_ord] += 1

            # reminder, we're adding tuples, and only care to return the values!
            res[tuple(key)].append(string)

        # listify the values!
        return list(res.values())
    
        