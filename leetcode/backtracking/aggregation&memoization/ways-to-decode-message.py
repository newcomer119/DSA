def decode_ways(digits: str) -> int:
    memo: dict[int, int] = {}

    def dfs(start_index: int) -> int:
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            return 1

        ways = 0
        # can't decode string with leading 0
        if digits[start_index] == "0":
            return ways
        # decode one digit
        ways += dfs(start_index + 1)
        # decode two digits
        if 10 <= int(digits[start_index : start_index + 2]) <= 26:
            ways += dfs(start_index + 2)

        memo[start_index] = ways
        return ways

    return dfs(0)

    return dfs(0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("12", 2), ("226", 3), ("06", 0)]
    passed = 0
    for digits, exp in TESTS:
        got = decode_ways(digits)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {digits!r} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
