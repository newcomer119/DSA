# 1146. Snapshot Array
# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


class SnapshotArray:
    def __init__(self, n: int):
        self.histories = [[[-1 ,0 ]] for _ in range(n)]
        self.snap_id = 0
        # self.histories = [[[-1, 0]] for _ in range(n)]
        # self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # self.histories[index].append([self.snap_id, val])
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        # self.snap_id += 1
        # return self.snap_id - 1
        self.snap_id += 1
        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        l = 0
        r = len(self.histories[index]) - 1

        ans = -1

        while l <= r:
            mid = (l + r) // 2
            if self.histories[index][mid][0] <= snap_id:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1


        return self.histories[index][ans][1]


        # left = 0
        # right = len(self.histories[index]) - 1
        # pos = -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if self.histories[index][mid][0] <= snap_id:
        #         left = mid + 1
        #         pos = mid

        #     else:
        #         right = mid - 1

        # return self.histories[index][pos][1]


# --- Daily tests ---
if __name__ == "__main__":
    arr = SnapshotArray(3)
    arr.set(0, 5)
    snap0 = arr.snap()
    arr.set(0, 6)

    arr2 = SnapshotArray(2)
    arr2.set(1, 8)
    s0 = arr2.snap()
    arr2.set(1, 12)
    s1 = arr2.snap()

    tests = [
        ("leetcode example", arr.get(0, snap0), 5),
        ("snap0 value", arr2.get(1, s0), 8),
        ("snap1 value", arr2.get(1, s1), 12),
        ("default zero", arr2.get(0, s1), 0),
    ]
    passed = 0
    for name, got, expected in tests:
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {got} (expected {expected})")
    print(f"\n{passed}/{len(tests)} passed")