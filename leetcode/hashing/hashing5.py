# Count all such pairs (i,j) such that arr[i] - arr[j] == k (count of such pairs ) and (i < j)
def count_pairs_brute_force(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] - arr[j] == k:
                count += 1

    return count 


def count_with_pairs(arr, k):
    count = 0
    freq_map = {}
    for num in arr:
        target = num + k
        count += freq_map[target]
        freq_map[num] += 1

    return count 