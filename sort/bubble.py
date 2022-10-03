def bubble(li) :
    for i in range(1, len(li)):
        for j in range(0, len(li)-1) :
            if li[j] > li[j+1] :
                li[j], li[j+1] = li[j+1], li[j]
                
    return li
        
li = [10, 2, 1, 7, 4, 3, 0]
print(bubble(li)) # [0, 1, 2, 3, 4, 7, 10] 

# 안정 정렬
# 시간복잡도 O(n^2)