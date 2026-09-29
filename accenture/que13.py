def neighbor_score(s: str) -> int:
    """
    A=1, B=2, ..., Z=26

    First character:
        current * next

    Last character:
        current * previous

    Middle characters:
        previous + current + next

    Return the total score.
    """

    # Write your solution here

    total_score = 0
    values =[]
    a = ord("A")
    for char in s:
        value = ord(char) - a + 1
        values.append(value)

    for i in range(len(values)):
        if i == 0:
            total_score += values[i] * values[i + 1]
        elif i == len(values) - 1:
            total_score += values[i] * values[i - 1]
        else:
            total_score += values[i-1] + values[i] + values[i + 1]
    return total_score


# ==========================================
# TEST CASES
# ==========================================

test_cases = [
    ("ABC", 14),
    ("AB", 4),
    ("AAA", 5),
    ("BCD", 27),
    ("AZ", 52),
    ("HELLO", 313),
]

# ==========================================
# TEST RUNNER
# ==========================================

for s, expected in test_cases:
    result = neighbor_score(s)

    print(f"s        = {s}")
    print(f"expected = {expected}")
    print(f"got      = {result}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")

    print("-" * 40)