# Count all such pairs (i,j) such that arr[i]  + arr[j] == k (count of such pairs ) and (i < j)

def count_pairs_brute_force(arr, k):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1

    return count 


def count_with_pairs(arr, k):
    count = 0
    seen = {}
    for num in arr:
        complement = num - k
        if complement in seen:
            count += 1

        seen[num] = True

    return count 