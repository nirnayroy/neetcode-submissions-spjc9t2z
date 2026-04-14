class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == []:
            return nums

        result = []
        def dfs(index, acc):
            current_sum = sum(acc)
            if current_sum > target:
                return
            elif current_sum == target:
                result.append(acc.copy())
                return
            else:
                for i in range(index, len(nums)):
                    acc.append(nums[i])
                    dfs(i, acc)
                    acc.pop()
                
        dfs(0, [])
        return result