class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. We want to sanitize, we do this by lower-casing the character
        # and only iterating through characters that are alphanumeric
        # We build an array of characters, then can use the ::-1 syntax to reverse it

        # it's possible I'm asked not to use .isalnum()
        left, right = 0, len(s) -1

        # we may be asked about the extra space and time; so double-pointer iteration is "better"
        while left < right:
            # the left < right guard looks redundant but as we're shifting the pos
            # it's possible to trip and land oob
            # traverse left until we find something good
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            # traverse rigt until we find something good
            while right > left and not self.isAlphaNumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            # don't forget to increment... cause I did...
            left += 1
            right -= 1

        return True



        # Note this is a bit of a cheat
        sanitized = [ch.lower() for ch in s if ch.isalnum()]
        return sanitized == sanitized[::-1]

        # leaving bad impl for questions
        # strip invalid characters
        # sanitized = [] * len(s)
        # for index, ch in enumerate(s):
        #     if ch.isalnum():
        #         sanitized[index] = ch.tolower()

        # left_to_right = "".join(sanitized)
        # right_to_left = "".join(reversed(sanitized))

        # return left_to_right == right_to_left

    def isAlphaNumeric(self, c):
        val = ord(c)
        return (ord('A') <= val <= ord('Z') or
         ord('a') <= val <= ord('z') or
         ord('0') <= val <= ord('9'))
        