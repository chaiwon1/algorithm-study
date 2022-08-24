# 일반적인 방식
def insert_normal(li) :
    for i in range(1, len(li)) : # 맨 왼쪽은 정렬되어있다고 생각해서 1부터 시작
        for j in range(i, 0, -1) :
            if li[j] < li[j-1] :
                li[j], li[j-1] = li[j-1], li[j]
            else :
                break
    return li

# 최적화
# 기존 값이 정렬된 상태에서 새롭게 비교할 값보다 작은 쪽은 비교도 안 하는 것.
def insert_opt(li) :
    for i in range(1, len(li)) :
        while i > 0 and li[i-1] > li[i] :
            li[i-1], li[i] = li[i], li[i-1]
            i -= 1
    return li


li = [10, 2, 1, 7, 4, 3, 0]
print(insert_normal(li)) # [0, 1, 2, 3, 4, 7, 10] 
print(insert_opt(li)) # [0, 1, 2, 3, 4, 7, 10] 

# 소량의 데이터를 정렬하기 좋음
# 탐색의 범위가 점점 넓어짐
# 시간 복잡도 O(n^2)