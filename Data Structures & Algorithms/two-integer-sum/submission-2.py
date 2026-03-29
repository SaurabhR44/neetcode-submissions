class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy_arr = []
        for i,num in enumerate(nums):
            copy_arr.append([num,i])
        copy_arr.sort()
        i,j = 0,len(nums)-1
        while i<j:
            cursor = copy_arr[i][0] + copy_arr[j][0]
            if cursor == target:
                return [min(copy_arr[i][1],copy_arr[j][1]),max(copy_arr[i][1],copy_arr[j][1])]
            elif cursor<target:
                i+=1
            else:
                j-=1
        return []

