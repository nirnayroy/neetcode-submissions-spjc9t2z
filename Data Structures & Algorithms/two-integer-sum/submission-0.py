class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for ind, num in enumerate(nums):
            diff_map[target-num] = ind
        
        for ind, num in enumerate(nums):
            if num in diff_map:
                if ind != diff_map[num]:
                    return [ind, diff_map[num]]