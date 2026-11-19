class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. We want to sanitize, we do this by lower-casing the character
        # and only iterating through characters that are alphanumeric
        # We build an array of characters, then can use the ::-1 syntax to reverse it

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
        