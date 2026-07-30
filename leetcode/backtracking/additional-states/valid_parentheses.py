# Generate All Valid Parentheses
# Given an integer n, generate all strings with n matching parentheses. "matching" parentheses mean

# there is equal number of opening and closing parentheses.
# each opening parenthesis has matching closing parentheses.
# For example, () is a valid string but )( is not a valid string because ) has no matching parenthesis before it and ( has no matching parenthesis after it.

# Input & Output
# Input
# n — number of matching parentheses
# Output
# all valid strings with n matching parentheses
# Example
# Input
# n = 2
# Output
# (())
# ()()
# Explanation
# There are two ways to create a string with 2 matching parentheses.

# Example
# Input
# n = 3
# Output
# ((()))
# (()())
# (())()
# ()(())
# ()()()
# Explanation
# There are 5 ways to create a string with 3 matching parentheses.

def generate_parentheses(n: int) -> list[str]:
    res = []
    path = []

    def dfs(start_index, open_count,close_count):
        if start_index ==  2 * n:
            res.append("".join(path))
            return 

        if open_count < n:
            path.append("(")
            dfs(start_index + 1, open_count + 1, close_count)
            path.pop()

        if close_count < open_count:
            path.append(")")
            dfs(start_index + 1,open_count, close_count + 1)
            path.pop()


    dfs(0,0,0)
    return res
    
    
    # res= []
    # path = []
    # def dfs(start_index,open_count,close_count):
    #     if start_index == 2 * n:
    #         res.append("".join(path))
    #         return 
    #     if open_count < n:
    #         path.append("(")
    #         dfs(start_index + 1,open_count + 1, close_count)
    #         path.pop()
    #     if close_count < open_count:
    #         path.append(")")
    #         dfs(start_index + 1,open_count,close_count + 1)
    #         path.pop()
    # dfs(0,0,0)
    # return res

# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(generate_parentheses(2))
    ok = got == ["(())", "()()"]
    print(f"[{'PASS' if ok else 'FAIL'}] n=2 -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
