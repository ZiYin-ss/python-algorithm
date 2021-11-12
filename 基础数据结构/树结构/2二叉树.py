from collections import deque
class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
root = e
print(root.lchild.rchild.data)
"""
    在堆的那个地方 那个二叉树是线性列表 在这个地方是链式列表
"""

#  前序遍历  这个思想是真牛逼  递归也是牛逼
#  再说一遍 这个递归真的不好理解 你得明白 一开始是什么
def pre_order(root):
    if root:
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)

# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

# 层序遍历
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue)>0:
        #  这个地方是这样的 队列先显示根节点 把左节点入队然后再右节点入队 然后pop出来左边的
        #  按照列表来看 其实就是先遍历第一层再遍历第二层  左节点的左子节点和右子节点是不是左先进 在右 这样出是出左边的
        #  是不是就是一层的  这一层里面的都进去 然后下一层都进去  依次是从左到右的啊
        #  不好说 好理解 多注意
        node =queue.popleft()
        print(node.data,end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


level_order(root)


