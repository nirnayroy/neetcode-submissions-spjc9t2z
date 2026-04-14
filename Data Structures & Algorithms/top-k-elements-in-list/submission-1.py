class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        
        return sorted(freq_dict.keys(), reverse=True, key = lambda x: freq_dict[x])[0:k]