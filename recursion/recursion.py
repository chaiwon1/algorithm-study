# 탐색
def search(li, begin, end, target) :
    if begin > end :
        return -1
    elif target == li[begin] :
        return begin
    else :
        return search(li, begin+1, end, target)
    
print(search([1,2,3,4,5], 0, 4, 3)) # 2

# 팩토리얼
def factorial(n) :
    if n ==  1 :
        return 1
    else :
        return n * factorial(n-1)
    
print(factorial(5)) # 120

# 제곱
def squared(x, n) :
    if n == 0 :
        return 1
    else :
        return x * squared(x, n-1)
    
print(squared(2, 10)) # 1024

# 피보나치 수열
def fibo(n) :
    if n == 0 or n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)

print(fibo(10)) # 89

# 최대공약수
def gdc(m, n) : 
    if m < n : # 받고 싶은 숫자는 n < m의 형태니까 여기서 한 번 정렬 해주고
        m, n = n, m
    if m % n == 0 : # 둘이 딱 나눠떨어지면 큰 쪽이 최대공약수일거니까 n
        return n
    else :
        return gdc(n, m%n)

print(gdc(12, 48)) # 12
print(gdc(20, 48)) # 4

# n부터 역순으로 0까지 출력
def print_to_zero_pos(n, result_list):
	if n == 0 :
		return result_list.append(0)
	else :
		result_list.append(n)
		return print_to_zero_pos(n-1, result_list)
     	
pos = int(input("input : ")) # 5
result_list = []
print_to_zero_pos(pos, result_list)
print(result_list) # [5,4,3,2,1,0]

# n부터 0까지 출력
def print_to_zero_neg(n, result_list):
	if n == 0 :
		return result_list.append(0)
	else :
		result_list.append(n)
		return print_to_zero_neg(n+1, result_list)

neg = int(input("input : ")) # -3
result_list_neg = []
print_to_zero_neg(neg, result_list_neg)
print(result_list_neg) #[-3,-2,-1,0]

# 음수든 양수든 오면 각각 처리
def print_to_zero_pos_neg(nums, dir):
    # dir이 비어있는 dictionary로 들어온 경우
    if dir == {}:
        # 숫자들이 ,로 연결된 문자열로 들어왔으므로 분리해서 list에 담아준다
        nums = nums.split(',')
        for num in nums:
            dir[num] = [] # dictionary에 들어온 숫자들을 key로 만들고 비어있는 list를 각각의 value로 만들어준다
            print_to_zero_pos_neg(int(num), dir[num]) # 재귀호출을 활용해 list에 값을 담아준다 
    else:
        # 이 경우 dir이 dictionary가 아니라 배열이므로 현재 숫자를 문자로 바꿔서 추가
        dir.append(str(nums))
        # 숫자가 0보다 작은 경우 1씩 더해가며 재귀호출 진행
        if nums < 0:
            print_to_zero_pos_neg(nums + 1, dir)
        # 숫자가 0보다 큰 경우 1씩 빼가며 재귀호출 진행
        elif nums > 0:
            print_to_zero_pos_neg(nums - 1, dir)
    return dir # 결과 dictionary 반환
        
            
        
    
res = {}
print_to_zero_pos_neg('-10,10,5,-5', res)
import pprint
pprint.pprint(res)