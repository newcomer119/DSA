# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/
#
# Same task must be separated by at least n idle/other-task intervals.
# Return minimum CPU intervals to finish all tasks.
#
# Example: tasks = ["A","A","A","B","B","B"], n = 2 -> 8


from collections import Counter, deque
import heapq


def least_interval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    heap = []
    for count in counts.values():
        heapq.heappush(heap, -count)

    time = 0
    queue = deque()
    while heap or queue:
        time += 1
        if heap:
            count = heapq.heappop(heap)
            if count + 1 < 0:
                queue.append((count + 1, time + n))
        if queue and queue[0][1] == time:
            heapq.heappush(heap, queue.popleft()[0])
    return time


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "D", "B"], 1, 6),
        (["A", "A", "A", "B", "B", "B"], 3, 10),
    ]
    passed = 0
    for tasks, n, exp in TESTS:
        got = least_interval(tasks, n)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
