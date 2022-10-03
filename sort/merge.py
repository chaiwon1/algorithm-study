def merge(li) :
    if len(li) < 2 :
        return li
    
    mid = len(li) // 2
    left = merge(li[:mid])
    right = merge(li[mid:])
    
    output = []
    i = j = 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            output.append(left[i])
            i += 1
        else :
            output.append(right[j])
            j += 1
    output += left[i:]
    output += right[j:]
    return output
    

li = [10, 2, 1, 7, 4, 3, 0]
print(merge(li))

# 분할 정복의 정수
# 퀵 정렬보다는 느리지만 안정 정렬
# 시간복잡도 평균 O(nlogn)