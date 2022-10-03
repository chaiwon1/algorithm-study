from collections import deque

def radix(li) :
    dq = [deque() for _ in range(10)]
    
    max_val = max(li)
    q = deque(li)
    cur_ten = 1
    
    while max_val >= cur_ten :
        while q :
            num = q.popleft()
            dq[(num//cur_ten) % 10].append(num)
            
        for bucket in dq :
            while bucket :
                q.append(bucket.popleft())
                
        cur_ten *= 10
        
    return list(q)
        

li = [10, 2, 1, 7, 4, 3, 0]
print(radix(li)) # [0, 1, 2, 3, 4, 7, 10]

# 계수 정렬(counting sort)가 작은 범위(숫자들 사이의)에서 
# 효율적인데, 이걸 보완한 게 기수 정렬
# 시간 복잡도 O((n+k)* w(최대 자릿수))