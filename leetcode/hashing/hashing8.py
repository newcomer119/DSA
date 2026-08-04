# find the count of subarrays with sum equal to k  

# brute force 
def main():
    n = int(input("Enter the number of elements in the array: "))
    # Using 1-indexed style list matching your input logic
    arr = [0] * (n + 1)
    print("Enter elements of the array: ")

    for i in range(1, n + 1):
        arr[i] = int(input())

    k = int(input("Enter the value of k: "))
    count = 0
    
    # Check all possible subarrays (starting at j and ending at i)
    for j in range(1, n + 1):
        csum = 0
        for i in range(j, n + 1):
            csum += arr[i]
            if csum == k:
                count += 1

    print("The count of subarrays with sum equal to k is: ", count)



# Optimized with prefix and hashmap
def optimized_count(arr, k):
    # Initialize prefix_sum as a dictionary with sum 0 having a frequency of 1
    prefix_sum = {0: 1}
    current_sum = 0  # Avoid using 'sum' as it's a built-in Python function
    count = 0
    for num in arr:
        current_sum += num
        # Check if (current_sum - k) exists in our prefix sum dictionary
        if (current_sum - k) in prefix_sum:
            count += prefix_sum[current_sum - k]
        # Safely increment the frequency of current_sum
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return count