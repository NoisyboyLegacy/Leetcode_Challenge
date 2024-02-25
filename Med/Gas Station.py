def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    if sum(gas) < sum(cost):
        return -1
    curr_tank, start = 0,0
    for i in range(len(gas)):
        curr_tank += gas[i] - cost[i]
        if curr_tank <0:
            start += 1
            curr_tank = 0
    return start
print(canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))