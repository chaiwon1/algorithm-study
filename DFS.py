# 재귀를 활용한 DFS 구현하기 ver.1
dfs_graph = {  
    1: [2,3,4],
    2: [5],
    3: [6],
    4: [],
    5: [7],
    6: [5],
    7: [6],
}

def dfs_recur(node, dfs_list=[]):
    dfs_list.append(node)       # 리스트에 인접한 노드를 덧붙이는 형태

    for i in dfs_graph[node]:   # 노드의 인접한 노드를 기준으로 반복한다. 
        if i not in dfs_list :
            dfs_recur(i, dfs_list)

    return dfs_list

print(dfs_recur(2))  # 시작노드 
# [2, 5, 7, 6]


# 재귀를 활용한 DFS 구현하기 ver.2
dfs_graph = {  
    16: [12,13],
    12: [11,14],
    13: [19],
    11: [9],
     9: [91,92],
    91: [],
    92: [],
    14: [],
    13: [19],
    19: [15,20],
    15: [],
    20: [],
}

def dfs_recur(node, dfs_list=[]):
    dfs_list.append(node)   # 리스트에 인접한 노드를 덧붙이는 형태

    for i in dfs_graph[node]:   # 노드의 인접한 노드를 기준으로 반복한다. 
        if i not in dfs_list :
            dfs_recur(i, dfs_list)
            
    return dfs_list

print(dfs_recur(16))  # 시작노드
# [16, 12, 11, 9, 91, 92, 14, 13, 19, 15, 20]



# 스택을 활용한 DFS 구현하기 
dfs_graph = {  
    1: [2,3,4],
    2: [5],
    3: [6],
    4: [],
    5: [7],
    6: [5],
    7: [6],
}

def dfs_stack(start_node):
    dfs_list = []
    stack_list = [start_node]

    while stack_list:
        node = stack_list.pop() # 리스트 메소드
        if node not in dfs_list :
            dfs_list.append(node)
            for i in dfs_graph[node] :
                stack_list.append(i)

    return dfs_list 

print(dfs_stack(7))    # 시작노드
# [7, 6, 5]