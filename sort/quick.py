# 일반적인 방식
def quick_long(li, start, end) :
    def partition(start, end) :
        pivot = li[end]
        left = start
        
        # 리스트를 돌면서 pivot(여기서는 맨 끝 값)보다 작은 값(right)을 left(여기서는 첫 번째 값=기준점)이랑 swap
        for right in range(start, end) :
            if li[right] < pivot :
                li[left], li[right] = li[right], li[left]
                # 바꿔줬으면 left의 인덱스를 하나 추가해서 옆으로 옮겨줌,
                left += 1
        # for문 나오면 얼추 정렬이 끝나는데 현재 기준점left의 왼쪽엔 pivot보다 작은 값들만 모여있으니까 마지막에 left랑 pivot이랑 바꿔줌. 
        li[left], li[end] = li[end], li[left]
        # 그리고 left(처음 설정한 pivot의 인덱스)를 return 
        return left
    
    if start < end :
        pivot = partition(start, end)  # 얘는 함수호출
        quick_long(li, start, pivot-1) # 얘는 재귀
        quick_long(li, pivot+1, end)   # 얘도 재귀
        
    return li
          
    
# 파이쏘닉한 방식    
def quick_short(li) :
    if len(li) <= 1 :
        return li
    
    pivot = li[-1]
    head = li[:-1]
    
    left_side = [i for i in head if i <= pivot]
    right_side = [i for i in head if i > pivot]
    
    return quick_short(left_side) + [pivot] + quick_short(right_side)
        
    
li = [10, 2, 1, 7, 4, 3, 5]
li_one = [2]
print(quick_long(li, 0, len(li)-1)) # [1, 2, 3, 4, 5, 7, 10]
print(quick_long(li_one, 0, len(li_one)-1)) # [2]
print(quick_short(li)) # [1, 2, 3, 4, 5, 7, 10]

# 피벗보다 크면 오른쪽 작으면 왼쪽
# 불안정 정렬
# 고르게 쪼개지면 시간복잡도 O(nlogn) 불균형(이미 정렬되어있거나)하면 O(n^2)