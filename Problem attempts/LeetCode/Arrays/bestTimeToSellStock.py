"""
Brute Force sol
"""
""" def maxProfit(arr):
    maxProfit = 0

    for currIdx in range(len(arr)):
        for nextIdx in range(currIdx+1, len(arr)):
            if arr[currIdx] > arr[nextIdx]:
                continue
            currProfit = arr[nextIdx] - arr[currIdx]
            if currProfit > maxProfit:
                maxProfit = currProfit

    
    return maxProfit """


"""
Sliding window
"""
def maxProfit(arr):
    maxProfit = 0
    start_idx = 0
    stop_idx = 1

    while stop_idx < len(arr):
        if arr[start_idx] < arr[stop_idx]:
            profit = arr[stop_idx] - arr[start_idx]
            maxProfit = max(profit, maxProfit)
        else:
            start_idx = stop_idx

        stop_idx +=1

    return maxProfit


arr = [7,1,5,3,6,4]

print(maxProfit(arr))