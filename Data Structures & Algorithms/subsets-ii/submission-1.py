class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        curr = []
        def dfs(i):
            if i>=len(nums):
                res.append(curr.copy())
                return
            
            #Include nums[i]
            curr.append(nums[i])
            dfs(i+1)

            #Skip untill we get a non-duplicate number
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res