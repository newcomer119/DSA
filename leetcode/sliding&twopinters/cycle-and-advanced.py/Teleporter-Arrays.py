# Teleporter Arrays
# You are given two sorted arrays of distinct integers, arr1, and arr2. Your goal is to start from the beginning of one array, and arrive at the end of one array (it could be the same array or not).

# For each step, you can either move forward a step on an array, or move to a square in the other array where the number is the same as the number in your current square ("teleportation"). Your total score is defined as the sum of all unique numbers that you have been on.

# Find the maximum score that you can get given the above rules. Since the result might be very large and cause overflow, return the maximum score modded by 10^9 + 7.

# Parameters
# arr1: A list of ordered, distinct integers.
# arr2: Another list of ordered, distinct integers.
# Result
# The maximum score possible, modded by 10^9 + 7.
# Examples
# Example 1
# Input: arr1 = [2, 4, 5, 8, 10], arr2 = [4, 6, 8, 9]

# Output: 30

# Explanation:



# Constraints
# 1 <= len(arr1), len(arr2) <= 50000
# 1 <= arr1[i], arr2[i] <= 10^7
# arr1[i] < arr1[j] for all i < j. Same goes for arr2.

MODULO_AMT = 10**9 + 7

def maximum_score(arr1: list[int], arr2: list[int]) -> int:
    # The max score, summed up and modded
    result = 0
    # The pointer points to the first array
    ptr1 = 0
    # The pointer points to the second array
    ptr2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    # The sum of the subarray between the previous teleporter and "ptr1"
    section_sum1 = 0
    # The sum of the subarray between the previous teleporter and "ptr2"
    section_sum2 = 0
    # As long as the two arrays are not both at the end, we advance the pointers
    while ptr1 < n1 or ptr2 < n2:
        # If they match, we sum up the max score of that section and the score of
        # the current position, then shrink result by using modulo
        # Reset the sums and move the pointers afterwards
        if ptr1 < n1 and ptr2 < n2 and arr1[ptr1] == arr2[ptr2]:
            result += max(section_sum1, section_sum2) + arr1[ptr1]
            result %= MODULO_AMT
            section_sum1 = 0
            section_sum2 = 0
            ptr1 += 1
            ptr2 += 1
            continue
        # If either "ptr1" reaches the end, or "ptr2" is smaller than "ptr1"
        # we move "ptr2" and keep track of the sum.
        if ptr1 == n1 or (ptr2 != n2 and arr1[ptr1] > arr2[ptr2]):
            section_sum2 += arr2[ptr2]
            ptr2 += 1
        # Otherwise, we move "ptr1" and keep track of that sum
        else:
            section_sum1 += arr1[ptr1]
            ptr1 += 1
    # Add the remaining max section sum to the result, then return the result
    # modulo
    result += max(section_sum1, section_sum2)
    return result % MODULO_AMT


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [([2, 4, 5, 8, 10], [4, 6, 8, 9], 30), ([1], [1], 1), ([1, 3, 5], [2, 4, 6], 12)]
    passed = 0
    for a1, a2, exp in TESTS:
        got = maximum_score(a1, a2)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] score={got} (expected {exp})")
    print(f"\n{passed}/{len(TESTS)} passed")