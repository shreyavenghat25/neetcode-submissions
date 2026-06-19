class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # add a 0 at the end representing the TOP (costs nothing)
        cost.append(0)

        # fill each position with minimum cost to reach it
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])

        # answer is at the last position (TOP)
        return cost[-1]   