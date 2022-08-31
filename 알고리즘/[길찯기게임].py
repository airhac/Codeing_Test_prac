import sys
sys.setrecursionlimit(10**6)
def pre_dfs(order, node_l, answer):
    node = order[0]
    idx = node_l.index(node)
    right = []
    left = []
    for i in range(1, len(order)):
        if node[0] > order[i][0]:
            left.append(order[i])
        else:
            right.append(order[i])
    answer.append(node[2])
    if left:
        pre_dfs(left, node_l[:idx], answer)
    if right:
        pre_dfs(right, node_l[idx + 1:], answer)
    return 
def post_dfs(order, node_l, answer):
    node = order[0]
    idx = node_l.index(node)
    right = []
    left = []
    for i in range(1, len(order)):
        if node[0] > order[i][0]:
            left.append(order[i])
        else:
            right.append(order[i])
    if left:
        post_dfs(left, node_l[:idx], answer)
    if right:
        post_dfs(right, node_l[idx + 1:], answer)
    answer.append(node[2])
    return 

def solution(nodeinfo):
    pre_prior = []
    post_prior = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    order = sorted(nodeinfo, key = lambda x : (-(x[1]), x[0]))
    node_l = sorted(nodeinfo)

    pre_dfs(order, node_l, pre_prior)
    post_dfs(order, node_l, post_prior)
    return [pre_prior, post_prior]
