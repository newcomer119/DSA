# Pruning Template 
# function dfs(start_index, path):
# if is_leaf(start_index):
#    report(path)
#    return
# for edge in get_edges(start_index):
#   # prune if needed
#   if not is_valid(edge):
#     continue
#   path.add(edge)
#   # increment start_index
#   dfs(start_index + len(edge), path)
#   path.pop()


# Given a string s, find all ways to partition it so that every substring is a palindrome. Return all possible palindrome partitions of s.

# Examples
# Example 1:
# Input: aab
# Output:
#   [
#   ["a","a","b"],
#   ["aa","b"]
#   ]

def partition(s: str) -> list[list[str]]:
    ans = []
    n = len(s)
    def is_palindrome(word):
        return word == word[::-1]

    def dfs(start_index,path):
        if start_index == n:
            ans.append(path[:])
            return 

        for end in range(start_index + 1, n + 1):
            prefix = s[start_index:end]
            if is_palindrome(prefix):
                dfs(end, path + [prefix])


    dfs(0,[])
    return ans
    # ans = []
    # n = len(s)
    # def is_palindrome(word):
    #     return word == word[::-1]
    # def dfs(start,path):
    #     if start == n:
    #         ans.append(path[:])
    #         return 
    #     for end in range(start + 1, n + 1):
    #         prefix = s[start:end]
    #         if is_palindrome(prefix):
    #             dfs(end,path + [prefix])

    # dfs(0,[])
    # return ans






# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(map(tuple, partition("aab")))
    exp = sorted(map(tuple, [["a", "a", "b"], ["aa", "b"]]))
    ok = got == exp
    print(f"[{'PASS' if ok else 'FAIL'}] partition('aab') -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
