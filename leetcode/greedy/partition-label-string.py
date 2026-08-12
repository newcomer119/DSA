# 763. Partition Labels
# https://leetcode.com/problems/partition-labels/
#
# Partition string into max parts so each letter appears in at most one part.
# Return sizes of each part.
#
# Example: s = "ababcbacadefegdehijhklij" -> [9, 7, 8]


def partition_labels(s: str) -> list[int]:
    last_occurrence = {char: i for i, char in enumerate(s)}
    result = []
    start = 0
    end = 0
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("caedbdedda", [1, 9]),
    ]
    passed = 0
    for s, exp in TESTS:
        got = partition_labels(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{s[:8]}...' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
