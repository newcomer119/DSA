# Dp and backtrack solution 

# def minimum_migration_time(n, standard, batch):

#     def solve(i):

#         if i == n:
#             return 0

#         if i == n - 1:
#             return standard[i]

#         return min(
#             standard[i] + solve(i + 1),
#             batch[i] + solve(i + 2)
#         )

#     return solve(0)

def minimum_migration_time(n, standard, batch):
    dp = {}

    def solve(i):
        if i == n:
            return 0

        if i == n - 1:
            return standard[i]

        if i in dp:
            return dp[i]

        dp[i] = min(
            standard[i] + solve(i + 1),
            batch[i] + solve(i + 2)
        )

        return dp[i]

    return solve(0)