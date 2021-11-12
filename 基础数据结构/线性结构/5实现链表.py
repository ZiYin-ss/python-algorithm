class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node

    return head

def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node

    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end='')
        lk = lk.next


lk = create_linklist_head([1, 2, 3])
print(lk.next.item)
"""
    链表的插入和删除
        插入很简单 要插入.next = 已插入.next  已插入.next = 要插入
        删除也不难 要删除 = 前面的.next  前面.next = 前面.next.next  del p 其实也就是改一下把中间的去一下 next改一下呗
    
    双向链表
        不就是一个next和一个prior 
        删除和创建 原理和上面是一样的
    
    顺序表和链表
        链表插入删除要快 内存分配灵活 O(1)  顺序表是O(n)
        是不是链表很像树和图啊
"""