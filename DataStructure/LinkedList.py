# 단방향 연결리스트
class Node :
    def __init__(self, value) :
        self.value = value
        self.next = None
    
class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.nodeCount = 0

    # 순회
    def traverse(self) :
        res = []
        curr = self.head
        while curr is not None :
            res.append(curr.value)
            curr = curr.next
        return res

    # 검색(k번째 value 찾기 ex: LinkedList의 7번째 원소 찾기)
    def get_node(self, k) :
        if k < 1 or k > self.nodeCount :
            return None

        i = 1
        curr = self.head
        while i < k :
            curr = curr.next
            i += 1

        return curr

    # 검색(value의 위치 찾기 ex: LinkedList에서 23의 위치 찾기)
    def search_node(self, value) :
        curr = self.head

        while curr :
            if curr.value == value :
                return curr
            else :
                curr = curr.next

        return curr

    # 삽입(k번째에 value 삽입)
    def add_node(self, k, newNode) :
        if k < 1 or k > self.nodeCount + 1 :
            return None

        # 맨 앞 삽입
        if k == 1 :
            newNode.next = self.head
            self.head = newNode

        # 중간 삽입
        else : 
            if k == self.nodeCount + 1 :
                temp = self.tail
            else :
                temp = self.get_node(k-1)
                newNode.next = self.temp.next
                temp.next = newNode

        # 맨 뒤 삽입
        if k == self.nodeCount + 1 :
            self.tail = newNode

    # 삭제(k번째 원소 삭제 ex: 7번째 원소 삭제)
    def del_k(self, k) :
        if k < 1 or k > self.nodeCount :
            return None

        # 맨 앞 삭제
        if k == 1 :
            deleted = self.get_node(k)

            if self.nodeCount == 1 :
                self.head = None
                self.tail = None
                self.nodeCount = 0
            else :
                self.head = self.head.next
                self.nodeCount -= 1
            
            return deleted.value
        
        else :
            prev = self.get_node(k-1)

            # 중간 삭제
            prev.next = deleted.next

            # 맨 뒤 삭제
            if k == self.nodeCount :
                prev.next = None
                self.tail = prev
            
        self.nodeCount -= 1
        return deleted.value

    # 삭제(value 삭제 ex: 리스트 안의 23 삭제)
    def del_node(self, value) :
        if self.head == None :
            return None
        
        elif self.head.value == value :
            temp = self.head
            self.head = self.head.next
            del temp
        
        else : 
            curr = self.head
            while curr.next :
                if curr.next.value == value :
                    temp = curr.next
                    curr.next = curr.next.next
                    del temp
                else :
                    curr = curr.next
        return temp

    # 길이 구하기
    def get_length(self) :
        return self.nodeCount

    # 병합
    def concat(self, L) :
        self.tail.next = L.head
        if L.tail :
            self.tail = L.tail
        self.nodeCount += L.nodeCount



# 양방향 연결리스트
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    # 역방향 순회
    def reverse(self):
        res = []
        curr = self.tail
        while curr.prev.prev :
            curr = curr.prev
            res.append(curr.data)
        return res

    # 검색
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        # pos로 들어온게 head에 가까운지 tail에 가까운지 판별
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    # 삽입
    def insertAfter(self, prev, newNode):
        next = prev.next

        newNode.prev = prev
        newNode.next = next

        prev.next = newNode
        next.prev = newNode

        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        
        newNode.prev = prev
        newNode.next = next
        
        prev.next = newNode
        next.prev = newNode
        
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # 삭제
    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        
        prev.next = curr.next
        next.prev = curr.prev
        
        self.nodeCount -= 1
        return curr.data

    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        
        prev.next = curr.next
        next.prev = curr.prev
        
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        if pos is 1:
            return self.popAfter(self.head)
        else :
            prev = self.getAt(pos - 1)
            return self.popAfter(prev)

    # 병합
    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount