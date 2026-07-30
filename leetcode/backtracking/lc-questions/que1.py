# 93. Restore IP Addresses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


# Example 1:

# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:

# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:

# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def to_ip_address(path):
            address = path[0]
            for i in range(1, 4):
                address += "." + path[i]
            return address

        def get_edges(start_index):
            segments = []
            for i in range(start_index, start_index + 3):
                if i < len(s):    # if not out of bound
                    # up to and including s[i]
                    segments.append(s[start_index:i+1])
            return segments

        def is_valid(num):
            if num == "0":
                return True
            elif num[0] == "0":
                return False    # leading zero
            elif int(num) > 255:
                return False   # out of range
            else:
                return True

        def dfs(start_index, path):
            if len(path) > 4:
                return
            if start_index == len(s):   # if all digits are used
                if len(path) == 4:      # and there are exactly four segments
                    # add address to the result
                    ans.append(to_ip_address(path))
                return
            for edge in get_edges(start_index):
                if is_valid(edge):
                    path.append(edge)
                    dfs(start_index + len(edge), path)
                    path.pop()
        ans = []
        dfs(0, [])
        return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [("0000", ["0.0.0.0"]), ("1111", ["1.1.1.1"]), ("101023", [
        "1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])]
    passed = 0
    for s, exp in TESTS:
        got = sorted(sol.restoreIpAddresses(s))
        ok = got == sorted(exp)
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s} -> {len(got)} addresses")
    print(f"\n{passed}/{len(TESTS)} passed")
