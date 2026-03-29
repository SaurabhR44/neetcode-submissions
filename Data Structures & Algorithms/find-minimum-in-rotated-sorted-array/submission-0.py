class Solution:
    def findMin(self, nums: List[int]) -> int:
        newarr = sorted(nums)
        res = float("infinity")
        for num in nums:
            res = min(res,num)
        return res
