from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


#  栈解决
def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack)) > 0:
        curNode = stack[-1]  # 当前节点
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True

        for dir in dirs:
            # 这个地方是匿名函数找出当前节点的下一个节点的位置(上下左右)
            nextNode = dir(curNode[0], curNode[1])
            #  如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 2表示已经走过的
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False


# maze_path(1, 1, 8, 8)

"""
    解释这个地方
        从一个节点开始 任意找下一个能走的点 当找不到能走的点是 退回上一个点寻找是否有其他方向的点
        栈存储当前路径
        
        其实利用了深度优先搜索，你看那个for循环 一次循环 假如有就终止 去走下一个了 然后继续循环直到找到了 8，8这个坐标
        看里面的pop 是不假如4个都是2就把这个坐标pop出来  出栈下一个栈元素继续循环看看四周有没有 没有继续pop 找到有的就再走
        一直遍历  
        然后都没有的话 就说明没有这个坐标
        就这个意思 
        其实就不是说解决完 而是说设计一个算法 让他走 巧妙的走完之后你就发现 最后解决问题了 
"""


# 队列解决
def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]  # 根据当前节点第三个元素是下标 根据这个下标去取path列表里面对应的元素 依次
    realpath.append(curNode[0:2])  # 把起点放进去
    realpath.reverse()
    for node in realpath:
        print(node)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:  # 队空说明是死胡同
        curNode = queue.pop()  # 这个里面是存着节点路径
        path.append(curNode)  # 这个里面存着的是所有的路径
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                #  因为这个path保存的是谁带过来的 然后把索引值放这个地方存着的 过后会通过索引去找
                #  这个nextNode是不是对应的就是path里面最后一个元素curNode带过来的啊 看上面写的 确实是这样的
                maze[nextNode[0]][nextNode[1]] = 2
    #    其实这个地方你一直在想为什么没有pop出来 其实这个for循环执行了之后 你会发现 假如没有能走的
    #   就执行while了 然后就又会pop出来一个  就这样走呗 到最后有就执行print_r
    else:
        print("没有")
        return False


maze_path_queue(1, 1, 8, 8)

"""
    利用的是广度优先搜索
        从一个节点开始 寻找所有接下来能继续走的点 继续不断寻找 直到找到出口 
        创建一个东西 标记谁让谁来的
        
        这个最难的地方就是在于把所有的节点 都放到path里面  把节点和下标放到queue里面 然后pop到的时候保存path里面
        path根据每个元素的第三个元素更新一下 放到最终路径去
"""
