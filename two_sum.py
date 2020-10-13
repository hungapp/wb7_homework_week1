class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = dict()
        for i, n in enumerate(nums):
            to_find = target - n
            if to_find in passed:
                return [passed[to_find], i]
            passed[n] = i
