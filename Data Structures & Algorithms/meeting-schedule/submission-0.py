"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for n, cur_int in enumerate(sorted_intervals[:-1]):
            next_int = sorted_intervals[n+1]
            if next_int.start < cur_int.end:
                return False
        return True
