class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i==j:
                    continue
                prod*=nums[j]
            result[i] = prod
        return result