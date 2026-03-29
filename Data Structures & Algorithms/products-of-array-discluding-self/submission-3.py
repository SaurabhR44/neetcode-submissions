class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        n = len(nums)
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(n-2,-1,-1):
            postfix[i]=nums[i+1]*postfix[i+1]
        for i in range(n):
            res[i]=prefix[i]*postfix[i]
        return res
        