from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]

def xy_xmp(li):
    while True:
        exchange = False
        for i in range(len(li)-1):
            if li[i]+li[i+1] < li[i+1]+li[i]:
                li[i],li[i+1] = li[i+1],li[i]
                exchange = True
        if not exchange:
            return li

def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))
    # li列表的每个元素 str一下得到字符串返回的是一个列表 在list里面
    # 如果不用list是一个列表对象 无法正常显示列表
    li = xy_xmp(li)
    # li.sort(key=cmp_to_key(xy_cmp))
    # 其实这个地方不好理解 理解不了就算了  想排序 这个是不是就是一个快排
    #  这个函数真的不常用 不会就算了
    return "".join(li)


print(number_join(li))

"""
    有n个非负整数 将其按照字符串拼接的方式拼接为一个整数
    如何拼接可以得到最大的整数
    a+b if a+b>b+a else b+a

"""


"""
    假如有n个活动 这些活动要占用同一片场地 而场地在某时刻只能供一个活动使用
    开始时间是Si 结束时间fi  [Si,fi) si取到 fi取不到
    安排哪些活动能够使该场地举办的活动的个数最多
"""

activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
#  保证活动时间是按照结束时间排序好的  最先结束的 肯定是在最优解里面 这个是结论

def activity_selection(a):
    res = [a[0]]
    for i in range(1,len(a)):
        if a[i][0]>=res[-1][1]:  # 你就想 只能一个场地 那是不是res最后结束的时间一定要小于等于第二场开始的时间啊
            res.append(a[i])
    return res

print(activity_selection(activities))

