class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {val: inx for inx, val in enumerate(nums)}

        for i, num in enumerate(nums):
            diff = target - nums[i]

            if diff in values and values.get(diff) != i:
                return [i, values.get(diff)]