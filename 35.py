class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i,x in enumerate(nums):
            if x>=target:return i
        else:return len(nums)
