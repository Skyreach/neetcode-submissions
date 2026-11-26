class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer problem
        left, right = 0, len(s) - 1
        
        while left < right:
            # there's 2 conditions where we want to move pointers:
            # first, if the pointer is not alphaNumeric
            # second, when the match is the same
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            while right > left and not self.isAlphaNumeric(s[right]):
                right -= 1

            # We want to compare, but cannot if we've just moved pointers
            if s[left].lower() != s[right].lower():
                return False
            
            # I hekkin' forgot to increment again...
            left += 1
            right -= 1
        
        return True

    def isAlphaNumeric(self, c):
        val = ord(c)
        return (ord('A') <= val <= ord('Z') or
         ord('a') <= val <= ord('z') or
         ord('0') <= val <= ord('9'))
