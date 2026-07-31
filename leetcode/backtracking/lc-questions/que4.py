# 140. Word Break II
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:

# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []

# Constraints:
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def dfs(start_index, path):
            if start_index == len(s):
                ans.append("".join(path))
                return 

            for end in range(start_index, len(s)):
                w = s[start_index : end + 1]
                if w in wordDict:
                    path.append(w)
                    dfs(end + 1, path)
                    path.pop()


        dfs(0,[])
        return ans         
        # ans = []

        # def dfs(start_index, path):
        #     if start_index == len(s):
        #         ans.append(" ".join(path))
        #         return
        #     for end in range(start_index, len(s)):
        #         w = s[start_index: end + 1]
        #         if w in wordDict:
        #             path.append(w)
        #             dfs(end + 1, path)
        #             path.pop()

        # dfs(0, [])
        # return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    got = sorted(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    exp = ["cat sand dog", "cats and dog"]
    ok = got == sorted(exp)
    print(f"[{'PASS' if ok else 'FAIL'}] wordBreak -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
