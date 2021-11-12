#  冒泡排序
def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟 从零开始
        exchange = False
        # 设置标志位 假如里面真的修改了值 是不是改标志位 为true 如果一趟走完没有修改是不是就是说不需要修改了啊
        # 算是优化把
        for j in range(len(li) - i - 1):
            # 这个地方就是每趟之后就少了一个无序的列表 后面就增加了一个有序的 这个有序的长度不就是i的值呢
            # 还减一不就是和上面一样呗
            if li[j] > li[j + 1]:  # 要是降序 是吧符号改为小于号不就是的呢
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return
        #  其实这个代码不好理解 就是 走一趟 你想啊 假设共有9个 range(8) 只能访问列表的前八个 因为只需要比8次啊 最后一个是不用比的啊
        #  j是不是也是访问前8个 也是就是到第8个的时候 其实j还能访问到第9个 然后循环就结束了
        #  为什么有一个减i呢 因为比较来说 i每走了一趟 无序区不就减少了一个 不就是减去i吗 然后算无序区的不就好了


li = [3, 2, 4, 6, 5, 1, 8, 7, 9]
bubble_sort(li)
print(li)


# 选择排序
def select_sort_simple(li):
    #  这个不好 因为会生成两个列表  垃圾写法
    li_new = []
    #  这个会多个O(n)
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


# 选择排序 最优版本
def select_sort(li):
    for i in range(len(li) - 1):  # 少排一趟
        min_loc = i  # 设置最小位置的下标  这个是无序区的第一个呢
        for j in range(i + 1, len(li)):  # 和后面的比 加一是一个可做可不做的
            if li[j] < li[min_loc]:  # 这个遍历完之后 是不是把最小位置的下标给了min
                min_loc = j  # 这个时候min_loc 不就是最小下标了吗
        li[i], li[min_loc] = li[min_loc], li[i]  # 在这个地方做了替换呢


li1 = [3, 2, 4, 6, 5, 1, 8, 7, 9, 10]
select_sort(li1)
print(li1)


# 插入排序
def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1  # 指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            #  这个地方条件满足就会执行 不满足就算了
            #  意思就是当j大于0和当前手里元素大于摸到的牌
            #  就把当前这个li[j] 往后面移动一下
            #  然后j-=1 是继续向左比较
            #  继续执行这个条件
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp  # 上面的移动是不是就会在j+1的位置多了个空 上面的执行不了 就代表在这个中间啊
        # 自己走一遍 没那么简单 就是不好理解 代码量其实也少


li2 = [3, 2, 4, 6, 5, 1, 8, 7, 9, 11, 10]
insert_sort(li2)
print(li2)

"""
    内置函数
        sort(key = lambda x: x[1])
    排序lowB 三人组
        冒泡排序(Bubble Sort)
            列表每两个相邻的数，如果前面比后面大 则交换这两个数
            一趟排序完成后 则无序区减少一个数 有序区增加一个数
            假如在你第一趟排序走到一半 发现后面的比前面大了 你就拿后面这个大的继续后比 直到一次完毕 这样最大的是不是再最后面了啊
            一趟排序是不是就减少一个  趟数从0开始 一个列表运行 n-1趟
            O(n**2) 
                最好情况是O(n) 因为排序好了呗
        选择排序 select_sort
            第一次把列表中最小的拿出来 然后再来一次 依次循环 就排序了呗 
            可以放到一个新列表中 但是不好 会生成两个列表
            O(n**2)
        插入排序 insert_sort
            初始时有序区只有一个元素 每次从无序区摸一个元素插入到有序区中已有元素的正确位置
            O(n**2)
        总结
            O(n**2)效率怎么样呢 
            现在计算机大概是每秒运行10的7次方 10000000 一千万 那个一万的平方不就是一个亿 大概就是10秒
            还是慢
"""
