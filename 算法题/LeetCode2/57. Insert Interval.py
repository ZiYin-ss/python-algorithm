# 插入区间
"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
"""


class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], x[1]))
        return self.merge(intervals)

    def merge(self, intervals):
        result = []
        intervals.sort(key=lambda x: x[0])
        i = 0
        n = len(intervals)
        while i < n:
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if result:
                prev_start, prev_end = result[-1]
                hi = min(prev_end, cur_end)
                lo = cur_start
                if lo <= hi:
                    if cur_end > prev_end:
                        result[-1][1] = cur_end
                else:
                    result.append(intervals[i])
            else:
                result.append(intervals[i])
            i += 1
        return result

"""
    超级简单 就是把这个new列表加入进去 合并就可以了
"""