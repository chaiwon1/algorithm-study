def selection(li) :
    for i in range(0, len(li)-1) :
        min_index = i

        for j in range(i+1, len(li)) :
            if li[j] < li[min_index] :
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
        
    return li 
    
    
    
li = [10, 2, 1, 7, 4, 3, 0]
print(selection(li)) # [0, 1, 2, 3, 4, 7, 10]

# 불안정 정렬
# 시간 복잡도 O(n^2)