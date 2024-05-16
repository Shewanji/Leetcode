class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        startMap = {} # empty hashmap

        for k, v in enumerate(nums):
            diff = target - v
            if diff in startMap:
                return [startMap[diff], k]
            startMap[v] = k
        return
        