class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next  # 单纯看这个地方 十年也看不出来 你看下面的传进来的是什么就是Node类的一个实例
                #  然后就是把这个节点的next下一个的值重新赋值为当前self.node 是不是就可以一直取出来了
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s  # 这个过来了一个obj 其实就是把上一个的tail.next改为了这个obj啊
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:  # 这个地方是不是就是循环插入啊
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
            else:
                return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ",".join(map(str, self)) + ">>"  # 这个地方我总不需要说了把  self是可迭代的 变成str类型 逗号分割


"""
    哈希表是一种线性表的存储结构 哈希表由一个直接寻址表和一个哈希函数组成
    哈希函数h(k)将元素关键字k作为自变量 返回元素的存储下标
    
    有限的空间和无限的数据
        会将两个不同元素映射到同一个位置的情况 这个就叫哈希冲突
    解决
        开放寻址法
            线性探查 +1   二次探查 +1**2 -1**2 +2**2 -2**2
            二度哈希 多个哈希函数
        拉链法
            每个位置都连接一个链表 当冲突的时候 冲突的元素将被加到该位置链表的最后
    常见的哈希函数
        除法哈希法(k%m)，乘法哈希法，全域哈希法
        具体的实现就不说了 还有很多 直到就可以
"""

class HashTable:
    def __init__(self,size = 100):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self,k):
        return k%self.size

    def insert(self,k):
        i = self.h(k)
        if self.find(k):
            print("重复插入了")
        else: # 这个地方不是说直接就键值对了 而是先搞搞一个元素的插入 就这了
            self.T[i].append(k)

    def find(self,k):
        i = self.h(k)  # 这个i是不是就是经过加工之后这个k  所在的T的列表的那个索引啊
        return  self.T[i].find(k)  # 是LinkList的实例 有一个find方法查找这个链表里面有没有这个值啊

ht = HashTable()
ht.insert(0)
ht.insert(1)
print(",".join(map(str,ht.T)))


"""
    哈希表用的最多的就是 集合和字典 
    字典key 集合底层也是哈希函数
    MD5算法也是哈希的 解不出来 但是最恶心的就是相同的消息MD5值一样 
        也有人破解过
    文件的哈希值 根据两个文件的哈希值相同 则可认为文件是相同的
        用户可以利用他来验证下载的文件是否完整
        云存储服务商可以利用他来判断用户要上传的文件是否存在 从而实现妙传功能 
        假如这个视频和别人的视频一模一样 别人已经上传了 那么是不是就可以把这个目录给别人 但是视频别人的 自己也共享了 
        也是自己的 就是这个文件 整个百度云只有一份 然后自己上传了这个不是真的上传了 只是把别人的拿过来你用了 
        这个效率难道不高吗 很高的 牛逼
    SHA2算法
    DES
    3DES
    Blowfish
    国际数据加密算法（IDEA)
    DSA
    RSA
    这些都是流行的密码算法 
"""