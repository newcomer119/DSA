# A. Line Trip - Codeforces 1901A (800 rated)
# https://codeforces.com/contest/1901/problem/A

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))

    # Minimum tank = largest "hard" segment on the trip
    ans = stations[0]  # distance 0 -> first station

    for i in range(1, n):
        ans = max(ans, stations[i] - stations[i - 1])

    # Last segment is special: no gas at x, so you go x -> last station -> x
    ans = max(ans, 2 * (x - stations[-1]))

    print(ans)
