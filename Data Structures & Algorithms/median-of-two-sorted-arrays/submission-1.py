class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        totallen = len(merged)
        if totallen%2==0:
            return (merged[totallen//2] + merged[totallen//2 -1])/2
        else:
            return merged[totallen//2]