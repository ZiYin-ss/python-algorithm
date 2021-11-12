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

    def insert__no_rec(self, val):
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
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def __remove_node_21(self, node):
        if not node.parent:
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
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:
                self.__remove_node_21(node)
            elif not node.lchild:
                self.__remove_node_22(node)
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


"""
    AVL树 是一棵自平衡的二叉搜索树
        根的左右子树的高度之差的绝对值不能超过1
        根的左右子树都是平衡二叉树
    重点考虑的是怎么维护这个树
        旋转
            插入一个节点后 需要找到第一个破坏了平衡条件的节点 称之为k k的两棵子树的高度差2
        
        不平衡的四种情况
            对k的右孩子的右子树的插入导致的 左旋  右侧多两个不就左旋呗 想图  就是想想树的那个图片 就知道是左旋了 
            对k的左孩子的左子树插入导致的 右旋  左侧多两个不就右旋呗
            对k的右孩子的左子树插入导致的 右旋——左旋
            对k的左孩子的右子树插入导致的 左旋——右旋
                这个地方最后两个你可能想不出来 
                看图 你就知道为什么先左旋再右旋了
                因为先小子树右边多了 左旋之后 大子树左边多了 就右旋
            
            
"""


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def insert__no_rec(self, val):
        pass

    def rorate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        # 这个地方有一个问题 就是说要是这个c成为了p之后 原先p的父节点不也是c的父节点吗  那原先p要是别人的左节点或者右节点怎么写呢
        if p.parent:
            c.parent = p.parent
            if p.parent.lchild == p:
                p.parent.lchild = c
            elif p.parent.rchile == p:
                p.parent.rchild = c
        else:
            c.parent = None
        p.parent = c
        p.bf = 0  # 对于删除 这个bf不是0的 得改一下
        c.bf = 0

    def rorate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        if p.parent:
            c.parent = p.parent
            if p.parent.lchild == p:
                p.parent.lchild = c
            elif p.parent.rchile == p:
                p.parent.rchild = c
        else:
            c.parent = None
        p.parent = c
        p.bf = 0
        c.bf = 0

    def rotate_right_left(self, p, c):
        #  首先说一句 我们得目的是将二叉搜索树改为二叉平衡树 并不是说插入什么的 而是插入之后改树
        g = c.lchild
        self.rorate_right(c, g)  # 这个地方 执行完了之后 是不是g就已经取代了c的位置
        self.rorate_left(p, g)  # 这个地方 g是不是就在原来c的位置那 执行左旋的啊
        #  其实这个地方不用返回的 因为g.lchild不还是原来的那个吗  不影响的

    def rotate_left_right(self, p, c):
        #  首先说一句 我们得目的是将二叉搜索树改为二叉平衡树 并不是说插入什么的 而是插入之后改树
        g = c.lchild
        self.rorate_left(c, g)
        self.rorate_right(p, g)
        #  但是bf我一直没有更新 因为 不想改了 就这把
        #  这个就是平衡二叉树 我只是实现了旋转

"""
    这个二叉平衡树 
        是通过插入的时候 看bf的值 确定是否旋转
    扩展就是B-Tree
"""
