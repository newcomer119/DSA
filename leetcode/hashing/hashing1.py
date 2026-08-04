# You are given an array of N you are given Q queries and in each query you are 
# given a number X you need to tell the frequency of that number in the array


from collections import defaultdict

n = int(input())
arr = []
hash_map = defaultdict(int)

for i in range(0, n):
    num = int(input())
    arr.append(num)
    hash_map[num] += 1

q = int(input())
for i in range(0, q):
    query = int(input())
    count = hash_map[query]
    print(count)
