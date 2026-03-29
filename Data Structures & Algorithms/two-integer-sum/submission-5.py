class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,num in enumerate(nums):
            prevMap[num] = i
        for i,num in enumerate(nums):
            diff = target - nums[i]
            if diff in prevMap and prevMap[diff]!=i:
                return [i,prevMap[diff]]
        return []
        
       

