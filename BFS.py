bfs_graph = {   
    1: [2,3,4],
    2: [1,5,6],
    3: [1,6],
    4: [1],
    5: [6,7],
    6: [5],
    7: [6],
}

def bfs_queue(start_node) :
    bfs_list = []  # visited
    queue = [start_node] # need_visit

    while queue :
        node = queue.pop(0)
        for i in bfs_graph[node] :
            if i not in bfs_list :
                bfs_list.append(i)
                queue.append(i)

    return bfs_list

print(bfs_queue(2))
# [1, 5, 6, 2, 3, 4, 7]