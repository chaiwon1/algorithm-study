# 최대힙
def siftdown(li, i, size) :
    left = 2 * i + 1 # 왼쪽 자식노드
    right = 2 * i + 2 
    largest = i
    if left <= size-1 and li[left] > li[i] :
        largest = left
    if right <= size-1 and li[right] > li[i] :
        largest = right
    if largest != i :
        li[i], li[largest] = li[largest], li[i]
        siftdown(li, largest, size)

def heapify(li, size) :
    # 절반만 확인하면 됨
    p = (size//2)-1 
    while p>=0 :
        # 자식노드랑 확인하는 siftdown 함수 호출
        siftdown(li, p, size)
        p -= 1
    return li
    
li = [10, 2, 1, 7, 4, 3, 0]    
print(heapify(li, len(li))) # [10, 4, 3, 7, 2, 1, 0]

# 완전이진트리가 기본
# 시간복잡도 평균 O(nlogn)
# 참고 : https://ratsgo.github.io/data%20structure&algorithm/2017/09/27/heapsort/