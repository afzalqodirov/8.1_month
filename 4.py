class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x=sorted(nums1+nums2)
        y=len(x)
        return x[y//2] if y%2==1 else (x[y//2]+x[y//2-1])/2