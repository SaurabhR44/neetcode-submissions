class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num,0)
        heap = []
        for num in hash_map.keys():
            heapq.heappush(heap,(hash_map[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res 
