# we are given an array of numbers we need to find and print any number 
#  with maximum and minimum frequencies 

# n = int(input())
# a  = list(map(int, input().split()))

# min_freq = float('inf')
# max_freq = 0
# min_elem = -1
# max_elem = -1

# for i in range(n):
#     count = 0
#     for j in range(n):
#         if a[i] == a[j]:
#             count += 1
    
#     if count < min_freq:
#         count = min_freq
#         min_elem = a[i]


#     if count > max_freq:
#         count = max_freq
#         max_elem = a[i]

# print(min_elem, max_elem)


# Using hashmap 

n = int(input())
k = {}

for _ in range(n):
    y = int(input)
    k[y] = k.get(y,0) + 1

minFreq = float('inf')
maxFreq = 0
minElem = -1
maxElem = -1

for number , count in k.items():
    if count < minFreq:
        minFreq = count
        minElem = number

    if count > maxFreq:
        maxFreq = count
        maxElem = number

print(minElem, maxElem)
