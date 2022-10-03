class Node(object) :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    # 전위순회(preorder) : root -> 왼쪽 자식노드 -> 오른쪽 자식노드 
    def preorder(self):
        def _preorder(node):
            print(node.value, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
    
    # 중위순회(inorder) : 왼쪽 자식노드 -> root -> 오른쪽 자식노드
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.value, end=' ')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
    
    # 후위순회(postorder) : 왼쪽 자식노드 -> 오른쪽 자식노드 -> root 
    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.value, end=' ')
        _postorder(self.root)

"""
트리구조

                1
              /   \
            2      3
           / \    / \
         4   5   6   7
        /
      8
"""

# 노드 삽입

BT = BinaryTree()
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
N8 = Node(8)

BT.root = N1
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8


print('preorder')
BT.preorder() 
# preorder
# 1 2 4 8 5 3 6 7

print('\ninorder')
BT.inorder()
# inorder
# 8 4 2 5 1 6 3 7

print('\npostorder')
BT.postorder()
# postorder
# 8 4 5 2 6 7 3 1