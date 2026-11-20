class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_streak = 0

        charSet = set()

        # Sliding Window approach from neetcode
        l = 0
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                max_streak = max(max_streak, r - l + 1)

            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1

                charSet.add(s[r])
                max_streak = max(max_streak, r - l + 1)

            

        return max_streak

            



        # initial guess
        # iterating through the container
        # start at z, check next (iter); track with a set
        # after loop, increase pointer from z to x

        left, right = 0, 1 # left is the start, and right is the current sequence
        max_streak = 0

        if not bool(s): return 0
        
        streak_container = set() # has an issue with resetting
        
        # assume that left < right
        while right < len(s):
            
            streak_container.add(s[left])

            if s[right] in streak_container:
                streak = len(streak_container)

                max_streak = max(streak, max_streak)
                left += 1
                right = left + 1
                #reset the contianer
                streak_container = set()
            else:
                streak_container.add(s[right])
                right += 1

        return max_streak

            


            
        