class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharacterMap = {}
        tCharacterMap = {}

        for sChar in s:
            if sChar not in sCharacterMap:
                sCharacterMap[sChar] = 0
            else:
                sCharacterMap[sChar] += 1
        for tChar in t:
            if tChar not in tCharacterMap:
                tCharacterMap[tChar] = 0
            else:
                tCharacterMap[tChar] += 1


        if len(sCharacterMap) != len(tCharacterMap):
            return False

        for sKey, sValue in sCharacterMap.items():
            if sKey not in tCharacterMap:
                return False
            if tCharacterMap[sKey] != sValue:
                return False
        
        return True


        