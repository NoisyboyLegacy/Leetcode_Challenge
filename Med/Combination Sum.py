def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    stack = [(0, target, [])]
    while stack:
        cur_index, cur_target, cur_comb = stack.pop()
        while cur_index < len(candidates):
            cur_candi = candidates[cur_index]
            if cur_candi == cur_target:
                result.append(cur_comb + [cur_candi])
            elif cur_candi < cur_target:
                stack.append((cur_index, cur_target - cur_candi, cur_comb + [cur_candi]))
            cur_index += 1
    return result


print(combinationSum(candidates=[2, 3, 5], target=8))
