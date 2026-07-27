from typing import List

# Hint
# There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

# For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
# Return an integer array answer where answer[i] is the answer to the ith query.

 

# Example 1:

# ex-1
# Input: s = "**|**|***|", queries = [[2,5],[5,9]]
# Output: [2,3]
# Explanation:
# - queries[0] has two plates between candles.
# - queries[1] has three plates between candles.
# Example 2:

# ex-2
# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
# Output: [9,0,0,0,0]
# Explanation:
# - queries[0] has nine plates between candles.
# - The other queries have zero plates between candles.


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)

        res = []
        for qleft, qright in queries:
            left_pos, right_pos = -1, -1
            
            # 1. Find the first candle index >= qleft
            left, right = 0, len(candles) - 1
            while left <= right:
                mid = (left + right) // 2
                if candles[mid] >= qleft:
                    left_pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 2. Find the last candle index <= qright
            left, right = 0, len(candles) - 1
            while left <= right:
                mid = (left + right) // 2
                if candles[mid] <= qright:
                    right_pos = mid
                    left = mid + 1
                else:
                    right = mid - 1

            # Calculate result using the formula
            if left_pos != -1 and right_pos != -1 and right_pos > left_pos:
                res.append((candles[right_pos] - candles[left_pos]) - (right_pos - left_pos))
            else:
                res.append(0)

        return res


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        ("**|**|***|", [[2, 5], [5, 9]], [2, 3]),
        ("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]], [9, 0, 0, 0, 0]),
        ("*|***", [[0, 4]], [0]),
        ("*|", [[0, 1]], [0]),
    ]
    passed = 0
    for name, s, queries, expected in TESTS:
        got = sol.platesBetweenCandles(s, queries)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {got} (expected {expected})")
    print(f"\n{passed}/{len(TESTS)} passed")