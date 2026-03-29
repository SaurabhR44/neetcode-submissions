class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = float("infinity")
        for i in range(len(nums)):
            if target==nums[i]:
                 res = i
        return res if res!=float("infinity") else -1
        