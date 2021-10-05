def buy_and_sell(arr):

    if len(arr) == 0 or len(arr) == 1 or arr[0] == max(arr):
        return 0

    curr_idx, overall_max, profit = 0, 0, 0
    next_idx = 1
    pending_checks = len(arr) - 1

    while curr_idx < len(arr) - 1:
        profit = arr[next_idx] - arr[curr_idx]
        if profit > overall_max:
            overall_max = profit
        next_idx += 1
        pending_checks -= 1
        if pending_checks <= 0:
            curr_idx += 1
            next_idx = curr_idx + 1
            pending_checks = len(arr) - next_idx

    return overall_max


arr = [1, 11, 8, 5, 7, 10, 23, 60, 22, 62, 2, 40000]
print(buy_and_sell(arr))