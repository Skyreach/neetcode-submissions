class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # There's a couple approaches, we could use a map 'char': count; but we can use ord w/ arrays to exploit a smaller container.

        # build the signature of s as an anagram
        s_inventory = [0] * 26

        for character in s:
            relative_ord = ord(character) - ord('a')
            s_inventory[relative_ord] += 1

        # same for t
        t_inventory = [0] * 26

        for character in t:
            relative_ord = ord(character) - ord('a')
            t_inventory[relative_ord] += 1

        # we could convert to a tuple
        return tuple(s_inventory) == tuple(t_inventory)
        