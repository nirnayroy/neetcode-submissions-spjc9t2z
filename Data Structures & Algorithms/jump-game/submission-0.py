class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums)-1
        pos = dest - 1
        while pos > 0:
            if nums[pos] >= dest-pos:
                dest = pos
            pos -= 1
        if nums[pos] >= dest:
            return True
        else:
            return False