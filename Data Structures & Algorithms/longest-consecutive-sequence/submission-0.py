class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list_of_set = []
        max_len = 0
        for num in nums:
            if num-1 not in nums:
                sequence = [num]
                while num + 1 in nums:
                    sequence.append(num+1)
                    num += 1
                max_len = max(len(sequence), max_len)
        return max_len

