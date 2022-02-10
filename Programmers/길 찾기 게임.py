import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree():
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        self.cur_node = self.root
        while True:
            if data < self.cur_node.data:
                if self.cur_node.left:
                    self.cur_node = self.cur_node.left
                else:
                    self.cur_node.left = Node(data)
                    break
            else:
                if self.cur_node.right:
                    self.cur_node = self.cur_node.right
                else:
                    self.cur_node.right = Node(data)
                    break
        
def preorder(node, preArr, orderdict):
    if node:
        preArr.append(orderdict[node.data])
        preorder(node.left, preArr, orderdict)
        preorder(node.right, preArr, orderdict)

def postorder(node, postArr, orderdict):
    if node:
        postorder(node.left, postArr, orderdict)
        postorder(node.right, postArr, orderdict)
        postArr.append(orderdict[node.data])

def solution(nodeinfo):
    answer = []
    # 노드의 순서번호를 x좌표를 key로 딕셔너리에 저장
    orderdict = {}
    for i in range(1, len(nodeinfo)+1):
        orderdict[nodeinfo[i-1][0]] = i
    # nodeinfo를 y의 좌표값, x의 좌표값 순으로 정렬
    nodeinfo.sort(key=lambda x:(-x[1], x[0]))
    
    # 트리 구성
    root = Node(nodeinfo[0][0])
    binaryTree = BinaryTree(root)
    
    for i in range(1, len(nodeinfo)):
        binaryTree.insert(nodeinfo[i][0])
        
    preArr = []
    postArr = []
    preorder(root, preArr, orderdict)
    postorder(root, postArr, orderdict)
    
    answer.append(preArr)
    answer.append(postArr)
    
    return answer