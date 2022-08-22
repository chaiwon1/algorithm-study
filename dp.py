# 피보나치 수열

# 재귀 구조 브루트 포스 : 제일 오래걸리는 버전. 15번 연산
def fib1(n) :
    if n <= 1 :
        return n
    else :
        return fib1(n-1) + fib1(n-2) 

# 메모이제이션 : 하향식. 9번 연산. 우아함.
import collections
def fib2(n) :
    dp = collections.defaultdict(int)

    if n <= 1 :
        return n
    
    if dp[n] :
        return dp[n]
    dp[n] = fib2(n-1) + fib2(n-2)
    return dp[n]

# 타뷸레이션 : 상향식. 4번 연산. 직관적
def fib3(n) :
    dp = collections.defaultdict(int)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1) :
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 두 변수만 이용해 공간 절약 : 공간 복잡도 O(1)
def fib4(n) :
    x, y = 0, 1
    for i in range(0, n) :
        x, y = y, x+y
    return x





# 15kg까지 들어가는 베낭에 (가격, 무게)로 묶인 튜플 형태의 짐들을 최대한 높은 가격들의 물건들로 채울 것
# 단, Greedy문제와는 다르게 짐을 쪼갤 수 없다. 
def zero_one_knapsack(cargo) :
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1) :
        pack.append([])
        for c in range(capacity + 1) :
            if i == 0 or c == 0 :
                pack[i].append(0)
            elif cargo[i - 1][1] <= c :
                pack[i].append(
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        pack[i - 1][c]
                    ))
            else :
                pack[i].append(pack[i - 1][c])
                
    return pack[-1][-1]

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1,1),
    (2,2)
]

print(zero_one_knapsack(cargo)) # 15




# 집 도둑. 각 집에는 훔칠 수 있는 돈의 액수가 있다. 단 바로 옆의 집은 털 수 없다. 어떻게 털어야 최대로 많이 터는가.

# 재귀 구조 브루트 포스
def rob1(nums) :
    def _rob(i) :
        if i < 0 :
            return 0
        # 맨 끝에서부터 확인해서 i의 옆집과, i옆옆집과 i집에서 털 수 있는 금액을 비교해서 큰 값을 리턴
        return max(_rob(i - 1), _rob(i - 2) + nums[i])
    return _rob(len(nums) - 1)

print(rob1([9, 3, 9, 8])) # 18 단, 이 방법은 타임아웃으로 안 풀릴 것이다. 최적화를 해주자. 

# 타뷸레이션
def rob2(nums) :
    if not nums :
        return 0
    if len(nums) <= 2 :
        return max(nums)

    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)) :
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    print(dp)
    
    return dp.popitem()[1] # <- popitem은 딕셔너리의 키를 몰라도 빼낼 수 있다.

print(rob2([8,7,3,9])) # 17 