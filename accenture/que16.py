import math
def next_palindromic_square(n: int) -> int:
    """
    Find the smallest number GREATER than n that is:

    1. A perfect square
    2. A palindrome

    Return the difference between that number and n.
    """
    def is_palindrome(word):
        return word == word[::-1]
    # Write your solution here
    root = int(math.sqrt(n) + 1)
    while True:
        square = root * root 

        if is_palindrome(str(square)):
            return square - n

        root += 1

# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    (404, 80),   # 484 = 22^2
    (100, 21),   # 121 = 11^2
    (120, 1),    # 121
    (121, 363),  # next one is 484
]


for n, expected in test_cases:
    result = next_palindromic_square(n)

    print(f"n        = {n}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)