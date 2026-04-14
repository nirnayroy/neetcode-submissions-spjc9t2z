class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        res = []
        for i in range(len(intervals)):
            if new_end < intervals[i][0]:
                res.append([new_start, new_end])
                return res + intervals[i::]
            elif new_start > intervals[i][1]:
                res.append([intervals[i][0], intervals[i][1]])
            else:
                new_start = min(intervals[i][0], new_start)
                new_end = max(intervals[i][1], new_end)
        res.append([new_start, new_end])
            
        return res


