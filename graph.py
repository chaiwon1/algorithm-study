# case 1 (시작노드부터 끝노드까지 전부 탐색)
connection_info = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
        }

def search_route(connection_info, start_node, end_node, route=[]):
    # 1. route = ['B']
    # 2. route = ['B', 'C']
    # 3. route = ['B', 'C', 'D']
    route = route + [start_node]  

    # 1. pass
    # 2. pass
    # 3. start_node = 'D' , end_node = 'D'이니까 stop. 현재 route = ['B', 'C', 'D'] 반환
    if start_node == end_node:
        return route 
    
    # 1. pass
    # 2. pass
    if not connection_info.__contains__(start_node):
        return None 

    # 1. node = 'C', 'D'
    # 2. node = 'D'
    for node in connection_info[start_node]:  

        # 1. node = 'C' 이면 route = ['B']에 없으니까 재귀 호출
        # 2. node = 'D' 이면 route = ['B', 'C']에 없으니까 재귀 호출
        if node not in route :   
            # 1. new_route = search_route(connection_info, 'C', 'D', ['B'])
            # 2. new_route = search_route(connection_info, 'D', 'D', ['B', 'C'])           
            new_route = search_route(connection_info, node, end_node, route)

            # 3. new_route = ['B', 'C', 'D']
            # 2. new_route = ['B', 'C', 'D']
            # 1. new_route = ['B', 'C', 'D']
            if new_route :
                return new_route
   
    return None

search_route(connection_info, 'B', 'D') # ['B', 'C', 'D']





# case 2 (시작노드부터 끝노드까지 전부 탐색)
connection_info = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['E', 'F'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

def search_route(connection_info, start_node, end_node, route=[]):
    # 1. route = ['B']
    # 2. route = ['B', 'C']
    # 3. route = ['B', 'C', 'E']
    # 4. route = ['B', 'C', 'E', 'F']
    route = route + [start_node]  

    # 1. pass
    # 2. pass
    # 3. pass
    # 4. pass
    if start_node == end_node:
        return route 
    
    # 1. pass
    # 2. pass
    # 3. pass
    # 4. pass
    if not connection_info.__contains__(start_node):
        return None 

    # 1. node = 'C', 'D'
    # 2. node = 'E', 'F'
    # 3. node = 'F'
    # 4. node = 'C'
    for node in connection_info[start_node]:  

        # 1. node = 'C' 이면 route = ['B']에 없으니까 재귀 호출
        # 2. node = 'E' 이면 route = ['B', 'C']에 없으니까 재귀 호출
        # 3. node = 'F' 이면 route = ['B', 'C', 'E']에 없으니까 재귀 호출
        if node not in route :   
            # 1. new_route = search_route(connection_info, 'C', 'D', ['B'])
            # 2. new_route = search_route(connection_info, 'E', 'D', ['B', 'C']) 
            # 3. new_route = search_route(connection_info, 'F', 'D', ['B', 'C', 'E'])          
            new_route = search_route(connection_info, node, end_node, route)

            if new_route :
                return new_route

        # 4. node = 'C'가 route = ['B', 'C', 'E', 'F']에 있기 때문에 return None    
    return None

search_route(connection_info, 'B', 'D') # None





# case 3 (시작노드와 끝노드의 최단 경로 탐색)
connection_info = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']
        }

# 복잡해서 그냥 호출 순서대로 적음
def search_shortest_route(connection_info, start_node, end_node, route=[]):
    # 1. route = ['B']
    # 4. route = ['B', 'C']
    # 7. route = ['B', 'C', 'D']
    # 14. route = ['B', 'D']
    route = route + [start_node]

    # 8. return ['B', 'C', 'D']
    # 15. return ['B', 'D']
    if start_node == end_node:
        return route

    if not connection_info.__contains__(start_node):
        return None

    shortest = None

    # 2. route = ['B'], node = 'C'
    # 5. route = ['B', 'C'], node = 'D'
    # 12. route = ['B'], node = 'D'
    for node in connection_info[start_node]:

        if node in route :
            return None

        # 3. new_route = search_shortest_route(connection_info, 'C', 'D', ['B'])
        # 6. new_route = search_shortest_route(connection_info, 'D', 'D', ['B', 'C'])
        # 9. 6번의 new_route = ['B', 'C', 'D']
        # 13. new_route = search_shortest_route(connection_info, 'D', 'D', ['B'])
        # 16. 13번의 new_route = ['B', 'D']
        new_route = search_shortest_route(connection_info, node, end_node, route)

        # 10. 4번의 new_route = ['B', 'C', 'D'], shortest = None
        # 17. 10번의 new_route = ['B', 'D'], shortest = ['B', 'C', 'D']
        if new_route :

            # 11.  4번의 new_route = ['B', 'C', 'D'] = shortest
            if shortest is None :
                shortest = new_route

            # 18. 10번의 len(new_route) = len(shortest) 2 < 3이기 때문에 shortest = ['B', 'D']
            elif len(new_route) < len(shortest):
                shortest = new_route

    # 19. 현재 shortest = ['B', 'D']
    return shortest

search_shortest_route(connection_info, 'B', 'D') # ['B', 'D']