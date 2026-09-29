def first_unique_character(s: str) -> str:
    """
    Return the first character that occurs exactly once.

    If there is no unique character, return "#".
    """

    # Write your solution here

    freq = {}

    # Step 1: count EVERY character
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: find FIRST character with count 1
    for char in s:
        if freq[char] == 1:
            return char

    # Step 3: none found
    return "#"


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ("accenture", "a"),
    ("aabbcddee", "c"),
    ("aabbcc", "#"),
    ("leetcode", "l"),
    ("swiss", "w"),
    ("x", "x"),
    ("aabbccd", "d"),
]


# ==========================================
# TEST RUNNER
# ==========================================

for s, expected in test_cases:
    result = first_unique_character(s)

    print(f"s        = {s}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)
