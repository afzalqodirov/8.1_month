class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        a = {}
        result = []
        for i,x in enumerate(heights):a[x]=names[i]
        for i in sorted(a.keys(), reverse=True):result.append(a[i])
        return result