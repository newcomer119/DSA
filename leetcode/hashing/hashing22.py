# Stable subarray with equal boundary and interior sum

def stableSubarray(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        isum = 0
        for j in range(i + 1, n):
            # If there is an interior element (j > i + 1)
            if j > i + 1:
                # Add the element just before j to the interior sum
                isum += nums[j - 1]
                # Check if boundaries are equal and interior sum equals the boundary value
                if nums[i] == nums[j] and isum == nums[i]:
                    count += 1
            else:
                # For j == i + 1, there are no interior elements, so interior sum is 0
                # (Depending on definition, if 0 == nums[i] when no interior exists, handle here if needed)
                pass
    return count


def countStableSubarray_optimized(capacity):
    g = {}
    total = 0
    ans= 0
    for c in capacity:
        total += c
        desired_sum = total - 2 * c
        if (desired_sum in g):
            ans += g[desired_sum]
        g[total] = g.get(total,0) + 1

    n = len(capacity)
    for i in range(n-1):
        if capacity[i] == 0 and capacity[i + 1] == 0:
            ans -= 1

    return ans 