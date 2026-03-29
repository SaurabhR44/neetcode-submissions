class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {num: frequency of times}
        hash_map = {}

        for num in nums:
            hash_map[num] = 1 + hash_map.get(num,0)
        
        pairs = []

        for num,cnt in hash_map.items():
            pairs.append([cnt,num])
        
        pairs.sort()
        res = []
        while len(res)<k:
            res.append(pairs.pop()[1])
        return res