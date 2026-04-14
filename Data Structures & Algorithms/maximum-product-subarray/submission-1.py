class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            new_max = max(n*cur_min, n*cur_max, n)
            new_min = min(n*cur_min, n*cur_max, n)
            cur_min, cur_max = new_min, new_max
            res = max(cur_max, res)
        return res
            