from typing import List


def knapsack_backtrack(weights: List[int], profits: List[int], W: int, n: int) -> int:
    """
    Solves the 0/1 Knapsack problem using backtracking (recursion).

    Parameters:
    weights (List[int]): List of item weights.
    profits (List[int]): List of item profits.
    W (int): Maximum capacity of the knapsack.
    n (int): Number of items to consider (typically len(weights)).

    Returns:
    int: Maximum profit achievable with given constraints.
    """
    # Base case: If no items left or no remaining capacity, profit is 0
    if n == 0 or W == 0:
        return 0

    # If the weight of the current item is more than the remaining capacity,
    # skip this item and move to the next
    if weights[n - 1] > W:
        return knapsack_backtrack(weights, profits, W, n - 1)
    else:
        # Case 1: Include the current item and add its profit
        include = profits[n - 1] + knapsack_backtrack(weights, profits, W - weights[n - 1], n - 1)
        # Case 2: Exclude the current item
        exclude = knapsack_backtrack(weights, profits, W, n - 1)
        # Return the maximum profit of the two cases
        return max(include, exclude)

def demo_knapsack_backtrack():
    weights: List[int] = [2, 3, 4, 5]  # Weights of the items
    profits: List[int] = [3, 4, 5, 6]  # Profits of the items
    W: int = 5  # Maximum capacity of the knapsack
    n: int = len(weights)  # Number of items

    # Calculate the maximum profit
    max_profit: int = knapsack_backtrack(weights, profits, W, n)
    print("Maximum profit:", max_profit)


def knapsack_dp(weights: List[int], profits: List[int], W: int) -> int:
    n = len(weights)
    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    profits[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

def demo_knapsack_dp():
    weights: List[int] = [2, 3, 4, 5]  # Weights of the items
    profits: List[int] = [3, 4, 5, 6]  # Profits of the items
    W: int = 5  # Maximum capacity of the knapsack
    n: int = len(weights)  # Number of items

    # Calculate the maximum profit
    max_profit: int = knapsack_dp(weights, profits, W)
    print("Maximum profit:", max_profit)

if __name__ == "__main__":
    demo_knapsack_backtrack()
    demo_knapsack_dp()