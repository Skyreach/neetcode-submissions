class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Given a string s contianing uppercase english caracters and k; we can do up to K subs
        # to find the longest string.
        # this looks like a Sliding Window problem
        # Starting with L, R = 0
        # We iterate through R, if the string is valid we can increment R
        # If the string is invalid, we move L

        # What's valid? It would have to be the run_length - max_seen <= k

        res = 0
        count = {}

        left = 0

        for right in range(len(s)):
            # increment what we've seen
            count[s[right]] = count.get(s[right], 0) + 1

            # if invalid, we need to decrement the left's count and move left
            # note: if you move conditions (like run or subs_needed) out of the check
            # we need to recalculate
            while right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # if valid, we can assign our result to the highest we've seen
            res = max(res, right - left + 1)

        return res