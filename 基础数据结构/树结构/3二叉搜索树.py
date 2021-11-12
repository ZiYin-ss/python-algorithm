from collections import deque
import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert__no_rec(val)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.prent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.prent = node
        return node

    def insert__no_rec(self, val):  # 非递归的快
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    def __remove_node_1(self, node):
        # 删除 情况1
        #  node是叶子节点
        if not node.parent:
            #  这个是判断是不是删除的是不是根节点
            #  根节点不就没有父节点吗 直接情况整个树呗
            self.root = None
        if node == node.parent.lchild:  # node是他父亲的左孩子
            node.parent.lchild = None
            # 变成none 其实并不是真正的物理删除了 只是下次查找的时候 是不是就是说找不到这个节点了啊
            # 因为p.lchild = None吗 这样不就找不到了吗
        else:  # node是他父亲的右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        #  node只有一个左孩子
        if not node.parent:  # 判断根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        elif node == node.parent.rchild:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        #  node只有一个右孩子
        if not node.parent:  # 判断根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        elif node == node.parent.rchild:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)  # 这个查询你得结合插入去想 插入的都是对象 查询的这个值 返回的不也是对象吗
            if not node:  # 不存在
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:  # 只有一个左孩子 这个地方只有一个左和右 其实左孩子或者右孩子 都可以还有孩子 因为不影响
                self.__remove_node_21(node)
            elif not node.lchild:  # 只有一个右孩子
                self.__remove_node_22(node)
            else:  # 两个孩子都有
                min_node = node.rchild
                while min_node.lchild:  # 一直找到最左端的节点
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                #  这个地方真tm牛逼 你看 找最左端的 那么是不是说只可能有右孩子 就执行这个22这个方法  删除右孩子
                #  也有可能叶子节点 直接执行1这个函数 就可以了
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

li = list(range(0, 500, 2))
random.shuffle(li)
tree = BST(li)
print(tree.query_no_rec(4).data)
tree.delete(4)
print(tree.query_no_rec(4))


""" 
    二叉搜索树 BST
        首先一颗树 
        假设x是父结点 y是左子节点   y.key<=x.key 
        假如y是右子节点 y.key>=x.key
        二叉搜索树 方便插入 插入删除查询 一半就没了吗
        深度说一下啊
            你看我自己写的二叉搜索树的时候 插入的时候是不是已经确定了左边的比右边小 
            所以可以确定的是  无论怎么插入怎么寻址 左边的都比右边小 
            左边的整个分支树 其实都比右边小 比右边最小的都小
            因为是不是一层一层的判定的 
            所以说你会发现走中序遍历 左中右的时候 就是升序
        
    删除操作分析
        删除叶子节点 直接删除
        删除的节点只有一个孩子 将此节点的父亲与孩子连接 然后删除该节点    但是孩子还可以有孩子 因为不影响
        如果要删除的节点有两个孩子 将其右子树的最小节点(最多有一个右孩子)删除 并替换当前节点
            就是最左端的节点 这个节点没有左孩子  因为要不然就不叫最左端的节点啊
            
    Tips:
        递归其实从上到下不好理解  
        但是从下到上很好理解 你想最后会形成什么 然后往上走一步 再走一步  这就是递归 
    
    二叉搜索树进行搜索的复杂度是O(logn)
    最坏就是非常偏斜 就是O(n)
    解决方法
        随机化插入
        AVL树
"""
