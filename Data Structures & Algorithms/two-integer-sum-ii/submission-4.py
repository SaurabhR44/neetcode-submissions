class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)
        for i in range(len(numbers)):
            find = target - numbers[i]
            if hmap[find]:
                return [hmap[find],i+1]
            hmap[numbers[i]] = i+1
        return []
