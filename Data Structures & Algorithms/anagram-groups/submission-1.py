import math
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # thoughts: Having a method that checks 2 strings and confirms it's an anagram
        # thought 2: If we can key the characters to make them logically equivalent this would be super fast
        # Looks like we can do ord.

        result = defaultdict(list) # hashedOrd : []

        for input in strs:
            product = math.prod(map(hash, input))
            result[product].append(input)

        return list(result.values())

    
        