class Solution:
    # NeetCode's approach is to have a 2-part delimiter
    # {wordLength}{delimiter}
    def encode(self, strs: List[str]) -> str:
        delim = "="
        parts = []
        for val in strs:
            wordLen = str(len(val))
            parts.append(wordLen)
            parts.append(delim)
            parts.append(val)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        delim = "="

        while i < len(s):
            j = s.index(delim, i)
            length = int(s[i:j]) # Up to but not including J
            startOfNext = j + length + 1
            res.append(s[j + 1 : startOfNext])
            i = startOfNext

        return res