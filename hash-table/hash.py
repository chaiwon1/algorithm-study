# 해시함수
def my_hashing_func(str, list_size):
    bytes_representation = str.encode()    
    sum = 0
    for byte in bytes_representation:
        sum += byte

    print('sum:', sum)
    print('list_size', list_size)
    print('sum % list_size:', sum % list_size)
    print()
    return sum % list_size

my_list = [None] * 5

# 해시테이블 값을 입력
my_list[my_hashing_func("aqua", len(my_list))] = "#00FFFF" # 해시 밸류 : 4
my_list[my_hashing_func("greeeeen", len(my_list))] = "#11FFFF" # 해시 밸류 : 2
my_list[my_hashing_func("red", len(my_list))] = "#22FFFF" # 해시 밸류 : 0

# 전체 해시테이블 출력
print(my_list) 
# ['#22FFFF', None, '#11FFFF', None, '#00FFFF']




# 해시 충돌을 위한 체이닝

chain_hash_table = [[] for _ in range(10)]  # 이번에는 10의 길이로 테스트를 진행한다.(0~9, 총 10개의 인덱스)
print(chain_hash_table)
# [[], [], [], [], [], [], [], [], [], []]

# 해시 함수
def chain_hash_func(key):
    return key % len(chain_hash_table)

# 체이닝 (extend 메서드를 활용해 연결리스트를 구현했다고 생각)
def chain_insert_func(chain_hash_table, key, value):
    hash_key = chain_hash_func(key)
    chain_hash_table[hash_key].extend(value)
    
chain_insert_func(chain_hash_table, 10, 'A') # 0번 인덱스에 'A' 들어감
print(chain_hash_table)
# [['A'], [], [], [], [], [], [], [], [], []]

chain_insert_func(chain_hash_table, 25, 'B') # 5번 인덱스에 'B' 들어감
print(chain_hash_table)
# [['A'], [], [], [], [], ['B'], [], [], [], []]

chain_insert_func(chain_hash_table, 20, 'C') # 0번 인덱스에 'C' 추가됨
print(chain_hash_table)
# [['A', 'C'], [], [], [], [], ['B'], [], [], [], []]





# 클래스로 구현

# 기능1) 아래 전체 함수를 포함하는 클래스
class hash_table:
    # 기능2) 키에 따른 값을 담아주는 함수
    def __init__(self):
        self.table = list([0 for _ in range(10)])
    

    # 기능3) name에 따라 특정값을 반환해주는 해시함수
    def hash_function(self, name) :
        return ord(name[0]) % 10


    # 기능4) name에 따라 num이 매칭되도록 설정하는 함수
    def hash_put(self, name, num):
        hash_address = self.hash_function(name)
        self.table[hash_address] = num


    # 기능5) name에 따라 매칭되는 num을 찾아주는 함수
    def hash_search(self, name):
        hash_address = self.hash_function(name)
        return self.table[hash_address]
    
    


# 입력값에 따른 출력값을 해시함수로 구현
"""
예상입출력값
        케이스1)
        입력 : [7,2,4,5], 12
        출력 : [(5, 7)]

        케이스2)
        입력 : [12,3,9,0], 12
        출력 : [(9, 3), (0, 12)]


"""

def hashing_sum(hashing_list, sum_value):
    hash_table = [None] * len(hashing_list)
    hashing_result = []
    
    # 변수 이름이 길어서 그냥 이중for문 쓰는 걸로
    for i in range(len(hashing_list)) :
        for j in range(i+1, len(hashing_list)) :
            if hashing_list[i] + hashing_list[j] == sum_value :
                hashing_result.append((hashing_list[i], hashing_list[j]))
                
    hash_table[hashing_list] = hashing_result

    return hashing_result