# count such pairs (i,j) such that abs(arr[i] - arr[j]) == k (count of such pairs ) and (i < j)
def count_pairs_brute_force(arr, k):
    n = len(arr)
    count = 0  # Added initialization
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) == k:
                count += 1
    return count
    
    
    
def count_pairs(arr,k):
    count = 0
    freq_map = {}
    for j in range(len(arr)):
        if arr[j] - k in freq_map:
            count += freq_map[arr[j] - k]
        if k != 0 and arr[j] + k in freq_map:
            count += freq_map[arr[j] + k]
        if arr[j] in freq_map:
            freq_map[arr[j]] += 1
        else:
            freq_map[arr[j]] = 1

    return count 