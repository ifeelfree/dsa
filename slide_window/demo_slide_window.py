def max_profit(prices):
    left = 0  # buy
    right = 1  # sell
    max_profit = 0
    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit

        right = right + 1

    return max_profit


def maxSumSubarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


if __name__ == "__main__":
    print(maxSumSubarray([1, 7, 2, 5, 8, 3], 2))