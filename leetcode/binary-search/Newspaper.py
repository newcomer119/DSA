# Newspapers
# You have a stack of newspapers in a fixed order. Each newspaper has a read time. You want to assign all newspapers to a group of at most num_coworkers workers. Each worker is assigned a consecutive section of newspapers from the stack, and all workers read their assigned sections in parallel.

# The constraint: you cannot reorder newspapers. If you assign newspapers at positions 1, 2, 3 to worker A, you cannot then assign newspaper 2 to worker B. Each worker gets a consecutive block from the original stack.

# Find the minimum time needed to read all newspapers. Since workers read in parallel, the total time equals the time taken by the slowest worker.

# For example, with newspapers [7,2,5,10,8] and 2 workers, you could assign [7,2,5] to worker A (14 minutes total) and [10,8] to worker B (18 minutes total). Worker B finishes last, so the answer is 18 minutes.

# Constraints
# 1 <= newspapers_read_times.length <= 10^5

# 1 <= newspapers_read_times[i] <= 10^5

# 1 <= num_coworkers <= 10^5

# Examples
# Example 1:
# Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
# Output: 18
# Explanation:
# Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.

# Example 2:
# Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
# Output: 7
# Explanation:
# Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.


def feasible(newspapers_read_times, num_coworkers, limit):
    num_workers = 1  # Start with 1 worker
    current_time = 0
    
    for read_time in newspapers_read_times:
        # If adding this newspaper exceeds the limit, 
        # this worker is done. A NEW worker starts with this paper.
        if current_time + read_time > limit:
            num_workers += 1
            current_time = read_time
        else:
            # Current worker can take this paper
            current_time += read_time
            
    # Return True if we used at most the allowed number of coworkers
    return num_workers <= num_coworkers

def newspapers_split(newspapers_read_times: list[int], num_coworkers: int) -> int:
    low,high  = max(newspapers_read_times), sum(newspapers_read_times)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if feasible(newspapers_read_times,num_coworkers,mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([7, 2, 5, 10, 8], 2, 18),
        ([2, 3, 5, 7], 3, 7),
        ([4, 5, 6], 1, 15),
        ([4, 5, 6], 3, 6),
        ([10], 5, 10),
    ]
    passed = 0
    for times, workers, expected in TESTS:
        got = newspapers_split(times, workers)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] times={times}, workers={workers} -> {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")