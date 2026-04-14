class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif nums[0] < nums[-1]:
            return nums[0]
        else:
            l = 0
            r = len(nums)-1
            
            while l<=r:
                m = (l+r)//2
                if nums[m+1] < nums[m]:
                    return nums[m+1]
                elif nums[m] > nums[l]:
                    l = m
                else:
                    r = m
