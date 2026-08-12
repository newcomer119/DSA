# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
#
# Return minimum conference rooms needed for all meetings.
#
# Example: [[0,30],[5,10],[15,20]] -> 2


import heapq


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    heap = []
    max_rooms = 0
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        max_rooms = max(max_rooms, len(heap))
    return max_rooms


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [2, 6], [3, 7]], 3),
    ]
    passed = 0
    for intervals, exp in TESTS:
        got = min_meeting_rooms(intervals)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] rooms -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
