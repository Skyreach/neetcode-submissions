class Solution:

    # NeetCode's approach is to have a 2-part delimiter
    # {wordLength}{delimiter}
    def encode(self, strs: List[str]) -> str:
        delim = "="
        container = ""
        for val in strs:
            wordLen = str(len(val))
            container += wordLen
            container += delim
            container += val
        return container

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "=":
                j += 1
            length = int(s[i:j]) # Up to but not including J
            startOfNext = j + length + 1
            res.append(s[j + 1 : startOfNext])
            i = startOfNext

        return res