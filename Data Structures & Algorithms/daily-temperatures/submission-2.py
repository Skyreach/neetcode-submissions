class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures [30, 38, 30, 36, 35, 40, 28]
        # 1, 4, 1, 2, 1, 0, 0
        # brute force way
        # for i, if i+1 > t[i]; res[i]

        # left = 0; rigt = left+1
        # check; if yes, L+=1, r = L+1
        # if no, r+=1
        # @ end, L += 1
        
        res = [0] * len(temperatures)
        # From Neetcode, this problem is a "Monotonic Decreasing Stack Problem"

        # By using a stack, we have 2 scenarios, let's start at the first
        # [30], append to the stack
        # [30, 38], as it's GT (peek), we can resolve by the distance then append
        unresolved = [] # [temp, index] // this is where I biffed...
        for i, temp in enumerate(temperatures):
            while unresolved and temp > unresolved[-1][0]:
                stackT, stackInd = unresolved.pop()
                # calculate the distance
                res[stackInd] = i - stackInd

            unresolved.append([temp, i])   # add the new unresolved
                
        return res
