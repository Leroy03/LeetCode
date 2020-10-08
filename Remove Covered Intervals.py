class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        delete = []
        num = 1
        for i, j in intervals:
            for n in range(num, length):
                # print(i, j, intervals[n][0], intervals[n][1])
                        if i >= intervals[n][0] and j <= intervals[n][1]:
                            if [i, j] not in delete:
                                delete.append([i, j])
                            break
                            # length -= 1
                        if i <= intervals[n][0] and j >= intervals[n][1]:
                            if [intervals[n][0], intervals[n][1]] not in delete:
                                delete.append([intervals[n][0], intervals[n][1]])
            num += 1
        return len(intervals) - len(delete)
