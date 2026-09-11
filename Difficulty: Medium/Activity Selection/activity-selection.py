class Meeting:
    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position


class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        n = len(start)

        # Create Meeting objects
        meet = [Meeting(start[i], finish[i], i + 1) for i in range(n)]

        # Sort by end time
        meet.sort(key=lambda x: (x.end, x.start))

        count = 1
        lastTime = meet[0].end

        for i in range(1, n):
            if meet[i].start > lastTime:
                count += 1
                lastTime = meet[i].end

        return count