class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        prod = 1
        zero_cnt = 0
        for num in nums:
            if num==0:
                zero_cnt+=1
            else:
                prod*=num
        for i in range(len(nums)):
            if zero_cnt>1:
                result[i]=0
            
            elif zero_cnt==1:
                    result[i] =prod if nums[i]==0 else 0

            else:
                result[i] = prod//nums[i]
        return result