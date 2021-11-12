class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾
        self.front = 0  # 队首

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("queue is filled")

    #  这个是自己写了一个队列 其实 一个列表 你想 第一个是队头 是不是push一个 rear就会加一啊
    #  这样出一个是不是就是对头往后面移动一个呗 对应的出来  这样是不是就理解队列了
    #  所谓的环形队列 是不是就是队尾慢了 是到队头了呗 +1 取模不就是队头的索引呗
    #  如果满了你还加的话是不是就是 is_filled 加不进去啊
    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]  # 这个地方其实没有删 因为在不在不影响 会直接重新赋值的
        else:
            raise IndexError("queue is emoty")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
for i in range(4):
    q.push(i)
    print(q.queue)

print(q.pop())
q.push(4)

"""
    其实都看到这了 我一直都想说 
    这个算法我看第一遍的时候 真的觉得就是一个空中阁楼 大二的时候
    这个严格来说是第二遍 这个时候的感觉就是一半在空中 一半在地下 
    因为有些东西 我已经知道是怎摸样循环怎么样走的 有些东西我也能写出来 还有就是对边界也有一些印象了 
    但是有些还是云里雾里
    多说一遍 真的真的不要觉得很简单 也不要觉得学不会 
    最好的方法就是你看完代码 你自己走几遍 走的过程中 多提出问题 假如这个是这个怎么处理 那个那个怎么处理
    看别人是怎么处理的 其实都没什么 多走几遍就好了  
    多走几遍 看别人的处理 当你自己真正这个过程你能走通了 能解惑了 其实也真的理解了 
    跟着多敲 多思考
"""

from collections import deque

# 列表就是队列 队头就是列表的第一个元素 队尾就是最后一个元素 出队是从队头出 入队是从队尾入
q = deque()  # 创建队列 里面还可以列表初始化队列 第二个参数是最大长度  多了不会报错 只会把前面的pop出去
q.append(1)  # 入队 是不是就是入到最后面去了啊
print(q.popleft())  # 从左边出来啊
#  appendleft 队首进队 pop队尾出队

#  读取后五行
# with xxxx as f:
#    q = deque(f,n) # 这个f就是文件里面的数据 readline写入的  一行是列表的一个元素呗
#  也就是说会把前面的给pop掉 留下后面五个
