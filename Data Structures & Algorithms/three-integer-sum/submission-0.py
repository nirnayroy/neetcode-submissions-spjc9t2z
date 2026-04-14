class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for n, i in enumerate(nums):
            if i > 0:
                break
            
            if n > 0 and i == nums[n-1]:
                continue

            l, r = n+1, len(nums)-1
            while l<r:
                if nums[l] + nums[r] + i > 0:
                    r -= 1
                elif nums[l] + nums[r] + i < 0:
                    l += 1
                else:
                    result.append([nums[l], nums[r], i])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l< r:
                        l+=1
        
        return result