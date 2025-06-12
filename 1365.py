class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        tmp = sorted(nums)
        result = []
        for i in nums:result.append(tmp.index(i))
        return result