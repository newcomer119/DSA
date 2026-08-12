# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
#
# Count ways to decode a digit string (A=1 ... Z=26, no leading zeros).
#
# Example: "12" -> 2  ("1,2" and "12")


def num_decodings(digits: str) -> int:
    memo = {}

    def dfs(start_index: int) -> int:
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            return 1
        if digits[start_index] == "0":
            return 0

        ways = dfs(start_index + 1)
        if start_index + 1 < len(digits):
            two_digit = int(digits[start_index : start_index + 2])
            if 10 <= two_digit <= 26:
                ways += dfs(start_index + 2)

        memo[start_index] = ways
        return ways

    return dfs(0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("10", 1),
    ]
    passed = 0
    for digits, exp in TESTS:
        got = num_decodings(digits)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] '{digits}' -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
