# Given two strings, original and check, return the shortest substring of original that contains every character in check, including duplicates. If multiple valid substrings have the same length, return the lexicographically smallest one.

# Parameters
# original: The source string.
# check: The required characters.
# Result
# The minimum valid window in original.
# Examples
# Example 1
# Input: original = "cdbaebaecd", check = "abc"

# Output: baec

# Explanation: Both cdba and baec are valid windows of length 4. We return baec because it is lexicographically smaller.

# Constraints
# 1 <= len(check), len(original) <= 10^5
# original and check contain only uppercase and lowercase English letters. Characters are case-sensitive.



from collections import Counter, defaultdict

def get_minimum_window(original: str, check: str) -> str:
    m, n = len(original), len(check)
    if m < n:
        return ""

    check_count = Counter(check)
    required = len(check_count.keys())
    window_count: defaultdict[str, int] = defaultdict(int)
    best_start = -1
    best_length = m + 1
    satisfied = 0
    l = 0

    for r in range(m):
        # keep track only characters that appear in check
        if original[r] in check_count:
            window_count[original[r]] += 1
            if window_count[original[r]] == check_count[original[r]]:
                satisfied += 1
        while satisfied == required:  # valid window
            current_length = r - l + 1
            if (
                current_length < best_length
                or (
                    current_length == best_length
                    and original[l : r + 1]
                    < original[best_start : best_start + best_length]
                )
            ):
                best_start = l
                best_length = current_length
            if original[l] in check_count:  # delete only characters from check
                window_count[original[l]] -= 1
                # removing original[l] makes window dissatisfied
                if window_count[original[l]] < check_count[original[l]]:
                    satisfied -= 1
            l += 1

    return original[best_start : best_start + best_length] if best_start >= 0 else ""


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("cdbaebaecd", "abc", "baec"), ("a", "a", "a"), ("a", "aa", "")]
    passed = 0
    for orig, check, exp in TESTS:
        got = get_minimum_window(orig, check)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {orig}/{check} -> {got!r}")
    print(f"\n{passed}/{len(TESTS)} passed")