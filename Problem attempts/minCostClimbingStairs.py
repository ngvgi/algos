def minCostClimbingStairs(cost) -> int:
    if len(cost) == 1:
        return cost[0]
    
    if len(cost) == 2:
        if cost[1] < cost[0]:
            return cost[1]
        return 0

    running_cost = 0
    idx = 0
    
    if cost[idx] == cost[idx+1] or cost[idx + 1] < cost[idx]:
        running_cost+= cost[idx + 1]
    else:
        running_cost = cost[idx]
    
    cost = cost[idx + 1:]

    return running_cost + minCostClimbingStairs(cost)
    

cost = [10,15,20]
print(minCostClimbingStairs(cost))


        
        
        