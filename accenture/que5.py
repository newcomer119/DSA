def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome after
    ignoring spaces and capitalization.
    """

    # Write your solution here
    words = s.lower()
    words = words.replace(" ", "")
    
    return words == words[::-1]




# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ("Race Car", True),
    ("Hello", False),
    ("Never odd or even", True),
    ("madam", True),
    ("Accenture", False),
    ("A", True),
    ("nurses run", True),
]


# ==========================================
# TEST RUNNER
# ==========================================

for s, expected in test_cases:
    result = is_palindrome(s)

    print(f"s        = {s!r}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)