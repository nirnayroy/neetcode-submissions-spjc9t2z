class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}
        for word in strs:
            sorted_str = str(sorted(list(word)))
            if sorted_str in groups:
                groups[sorted_str].append(word)
                # groups[sorted_str] = word_list
            else:
                groups[sorted_str] = [word]
        
        return groups.values()