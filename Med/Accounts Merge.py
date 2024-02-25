from collections import defaultdict


def accountsMerge(accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    em_to_name = {}
    em_graph = defaultdict(set)
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            em_graph[acc[1]].add(email)
            em_graph[email].add(acc[1])
            em_to_name[email] = name
    visit = set()
    ans = []

    def dfs(cur_email, comp):
        if cur_email in visit:
            return
        visit.add(cur_email)
        comp.append(cur_email)
        for related_email in em_graph[cur_email]:
            if related_email not in visit:
                dfs(related_email, comp)
        return comp

    for email in em_graph:
        if email not in visit:
            component = []
            dfs(email, component)
            ans.append([em_to_name[email]] + sorted(component))
    return ans


print(accountsMerge(accounts=[["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                              ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                              ["John", "johnnybravo@mail.com"]]))
