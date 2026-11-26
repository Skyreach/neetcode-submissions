class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_by_frequency = {}

        for num in nums:
            nums_by_frequency[num] = nums_by_frequency.get(num, 0) + 1

        # we now need to organize it by highest frequency
        # heaps are usually how we do this, and we want a max_heap

        max_heap = [(-value, key) for (key, value) in nums_by_frequency.items()]
        heapq.heapify(max_heap)

        # finally we need to append to the output
        output = []
        for _ in range(k, 0, -1): # 2, 1, 0 does not run
            occ, value = heapq.heappop(max_heap)
            output.append(value)

        return output

        # We want to return the most frequent K elements to do this, we need to know how often each has occurred
        # AND order this in a way that we can fetch it to be returned in the correct presentation order

        # Things to consider: it's entirely possible for a tie; like [2,2,3,3] return top 2
        frequency_map = {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        # We can't use a heap if we don't have a way make a list, so, we can either make a new container and org by frequency
        # or we can make some tuples
        # this is a bit outside my python skill grade without a google
        heap = [(-val, key) for (key, val) in frequency_map.items()]
        heapq.heapify(heap)

        output = []
        for i in range(k, 0, -1):
            occ, val = heapq.heappop(heap)
            # occ, val = heap.pop() doesn't work because it fails to consider the container heap'd
            output.append(val)

        # print(output)

        return output