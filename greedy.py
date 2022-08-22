# 15kg까지 들어가는 베낭에 (가격, 무게)로 묶인 튜플 형태의 짐들을 최대한 높은 가격들의 물건들로 채울 것
def fractional_knapsack(cargo) :
    capacity = 15
    pack = []

    # 단가 계산해서 역순으로 배치
    for i in cargo :
        pack.append((round(i[0]/i[1],2), i[0], i[1]))
    pack.sort(reverse=True) # [(2.5, 10, 4), (2.0, 2, 1), (1.0, 2, 2), (1.0, 1, 1), (0.33, 4, 12)]

    total_value = 0
    for p in pack :
        # 단가 순서대로 베낭에 넣기 
        if capacity - p[2] >= 0 :
            capacity = capacity - p[2]
            total_value += p[1]
        
        # 만약 안 들어가면 쪼개서라도 넣기
        else :
            fraction = round(capacity / p[2],2)
            total_value = fraction * p[1]
            break
    return total_value

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1,1),
    (2,2)
]

print(fractional_knapsack(cargo)) # 2.32
    




# 주식을 사고팔기 가장 좋은 시점 
def max_profit(price) :
    result = 0
    # price 돌면서 i번째 보다 i+1번째가 더 높으면 그 차액을 result에 담기
    for i in range(len(price)-1) :
        if price[i + 1] > price[i] :
            result += price[i + 1] - price[i]
    return result

print(max_profit([7,1,5,3,4,6])) # 7 = (1->5 + 3->4 + 4->6)

# 좀 더 파이쏘닉한 버전
def max_profit2(price) :
    return sum(max(price[i+1]-price[i], 0) for i in range(len(price)-1))

print(max_profit2([7,1,5,3,4,6])) # 7





# 원형으로 연결된 주유소들. 각각 gas = [1,2,3,4,5] 를 갖고 있고 다음 주유소로 가기 위해서 [3,4,5,1,2]가 필요.
# 몇 번째 인덱스의 주유소부터 시작해서 다 돌 수 있는가
def canCompleteCircuit(gas, cost) :
    for start in range(len(gas)) :
        fuel = 0

        # start 지점부터 한 바퀴 도는 for문을 열어준다.
        for i in range(start, len(gas) + start) :

            # 인덱스는 i를 길이만큼으로 나눠줘서 다시 순환할 수 있게 해준다. 
            index = i % len(gas)

            can_travel = True
            # 해당 주유소의 gas와 남아있는 연료를 더해 다음 주유소로 향하기 위해 필요한 cost와 비교
            if gas[index] + fuel < cost[index] :
                can_travel = False
                break
            else :
                fuel += gas[index] - cost[index]
        if can_travel :
            return start
    return -1

gas = [1,2,3,4,5]
cost = [3,1,4,5,2]

print(canCompleteCircuit(gas, cost)) # 4 다만, 이 경우 for문이 두 개이므로 O(n^2)의 시간복잡도가 든다. 따라서 최적화가 필요하다. 

def canCompleteCircuit2(gas, cost) :
    # 애초에 gas의 총량보다 cost가 많으면 
    if sum(gas) < sum(cost) :
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)) :

        # 수학적 귀류법을 통해 False들을 제거해주면 남는 게 True니까 그걸 반환
        if gas[i] + fuel < cost[i] :
            # 위의 if가 true라는 뜻은 다음 주유소로 못 간다는 뜻이니까 start를 다음으로 넘겨줌
            start = i + 1
            fuel = 0
        else :
            fuel += gas[i] - cost[i]

    return start

gas = [1,2,3,4,5]
cost = [3,1,4,5,2]

print(canCompleteCircuit2(gas, cost)) # 4 이러면 for문이 한 개라 O(n)으로 최적화가 되었다. 





# 아이가 만족하는 쿠키 사이즈 g = [1,2,3], 쿠키의 사이즈 s = [1,1]의 경우 최대 몇 명의 아이에게 쿠키를 나눠줄 수 있는가.
def findContentChildren(g, s) :
    # 만족하는 쿠키 사이즈가 작은 아이부터 맞춰주기 위해 정렬
    g.sort()
    s.sort()

    child_i = cookie_j = 0

    # 아이와 쿠키 수가 최대치로 가기전까지 
    while child_i < len(g) and cookie_j < len(s) :
        # 만족하는 쿠키 사이즈와 진짜 쿠키 사이즈를 비교해서 진짜 쿠키 사이즈가 더 크면 다음 아이와 다음 쿠키로 넘어가기
        if s[cookie_j] >= g[child_i] :
            child_i += 1
        cookie_j += 1

    return child_i


g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s)) # 1

g = [2,3,2,5]
s = [1,3,4]
print(findContentChildren(g, s)) # 2