class MyCircularDeque :
    def __init__(self, k:int) :
        # head, tail 
        self.head, self.tail = ListNode(None), ListNode(None)
        # 최대 길이, 현재 길이 
        self.k, self.len = k, 0
        # 처음엔 head의 오른쪽은 tail, tail의 왼쪽은 head 
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        # 원래있던 node의 오른쪽을 찢어서 n으로 할당
        n = node.right
        # node 오른쪽에 새로운 거 삽입
        node.right = new
        # 이제 new의 왼쪽과 오른쪽을 정리
        new.left, new.right = node, n
        # n의 왼쪽에 new 할당해서 정리
        n.left = new

    def _del(self, node: ListNode) :
        # node의 오른쪽의 오른쪽을 n에 담아두고
        n = node.right.right
        # node의 오른쪽이 이제부터 n
        node.right = n
        # 그리고 n의 왼쪽에 원래 있던 노드를 선언해서 node.right를 없애버림
        n.left = node

    def insertFront(self, value:int) -> bool :
        if self.len == self.k :
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    
    def insertLast(self, value:int) -> bool :
        if self.len == self.k :
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool :
        if self.len == 0 :
            return False
        self.len -= 1
        self._del(self.head)
        return True
    
    def deleteLast(self) -> bool :
        if self.len == 0 :
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int :
        # head의 right 값을 반환. 만약 비어있다면 -1 반환
        return self.head.right.value if self.len else -1

    def getRear(self) -> int :
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool :
        return self.len == 0

    def isFull(self) -> bool :
        return self.len == self.k