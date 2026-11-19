class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # value : number of occs
        frequency = [[] for i in range(len(nums) + 1)]

        for val in nums:
            count[val] = 1 + count.get(val, 0)
        for key, val in count.items():
            frequency[val].append(key)

        res = []
        for index in range(len(frequency) -1, 0, -1):
            for n in frequency[index]:
                res.append(n)
                if len(res) == k:
                    return res


