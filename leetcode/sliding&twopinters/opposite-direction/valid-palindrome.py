# Valid Palindrome
# Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case. Examples:

# Input: Do geese see God? Output: True

# Input: Was it a car or a cat I saw? Output: True

# Input: A brown fox jumping over Output: False


def is_palindrome(s: str) -> bool:
    l,r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r-= 1

        if s[l].lower() != s[r].lower():
            return False 

        r-= 1
        l+= 1

    return True 
    # l,r = 0, len(s) - 1

    # while l  < r:
    #     while l < r and not s[l].isalnum():
    #         l += 1
    #     while l < r and not s[r].isalnum():
    #         r -= 1
    #     if s[l].lower() != s[r].lower():
    #         return False

    #     r -= 1
    #     l += 1

    # return True 

# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [("Do geese see God?", True), ("Was it a car or a cat I saw?", True), ("A brown fox jumping over", False)]
    passed = 0
    for s, exp in TESTS:
        got = is_palindrome(s)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {s!r} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")