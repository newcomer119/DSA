
# General All Permutations
# Given a string of unique letters, find all of its distinct permutations.

# Permutation means arranging things with an order. For example, permutations of [1, 2] are [1, 2] and [2, 1]. Permutations are best visualized with trees.



# The number of permutations is given by n! (we looked at factorial in Recursion Review). The way to think about permutation is to imagine you have a bag of 3 letters. Initially, you have 3 letters to choose from, you pick one out of the bag. Now you are left with 2 letters, you pick again now there's only 1 letter. The total number of choices is 3*2*1 = 6 (hence we have 6 leaf nodes in the above tree).

# Input & Output
# Input
# letters — a string of unique letters
# Output
# all of its distinct permutations
# Example
# Input
# letters = abc
# Output
# abc
# acb
# bac
# bca
# cab
# cba
# Explanation
# All permutations.

def permutations(letters: str) -> list[str]:
    res = []
    path = []
    used = [False] * len(letters)
    

    def dfs(start_index):
        if start_index == len(letters):
            res.append("".join(path))
            return 

        for i,letter in enumerate(letters):
            if used[i]:
                continue 
            path.append(letter)
            used[i] = True
            dfs(start_index + 1)
            path.pop()
            used[i] = False
        
    dfs(0)
    return res

    # res = []
    # path = []
    # used = [False] * len(letters)

    # def dfs(start_index):
    #     if start_index == len(letters):
    #         res.append("".join(path))
    #         return 


    #     for i, letter in enumerate(letters):
    #         if used[i]:
    #             continue
    #         path.append(letter)
    #         used[i] = True
    #         dfs(start_index + 1)
    #         path.pop()
    #         used[i] = False
    # dfs(0)
    # return res
        




# --- Daily tests ---
if __name__ == "__main__":
    got = sorted(permutations("ab"))
    ok = got == ["ab", "ba"]
    print(f"[{'PASS' if ok else 'FAIL'}] permutations('ab') -> {got}")
    print(f"\n{1 if ok else 0}/1 passed")
