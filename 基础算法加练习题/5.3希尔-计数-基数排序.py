# 希尔排序
def insert_sort_gep(li, gap):
    for i in range(gap, len(li)):  # 这个gab是不是就是分组之后 第二列开始的第一个值啊(头一个是需要和后面比较的值吗)
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        #  其实这个地方 当你走到d=1的时候 就是直接插入排序了 只是这个li此时是一个很有序但又不算有序的列表了
        insert_sort_gep(li, d)
        d //= 2


li = list(range(1000))
import random

random.shuffle(li)
print(li)
shell_sort(li)
print(li)


# 计数排序
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]  # 生成全部都是0的数吗 0-100 都可以取得到
    for val in li:
        count[val] += 1
    li.clear()
    for index, val in enumerate(count):
        # 这个地方不就是将index添加到li数组呗 添加val次
        for i in range(val):  # 这个地方虽然是两层循环 append(n) 但是这个地方val不算n 是val+val+val
            li.append(index)


li1 = [random.randint(0, 100) for _ in range(1000)]  # 生成一千个0-100的数
print(li1)
count_sort(li1)
print(li1)


# 桶排序
def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]  # 创建n个桶
    for var in li:   # n
        i = min(var // (max_num // n), n - 1)
        # i表示放到几号桶里面 还有就是说这个地方是不是就做了前面的桶确实要比后面的桶的数据小啊
        buckets[i].append(var)  # 把var添加到桶里面
        #  这个地方就是每次插入一次就直接从后面开始来一次排序
        for j in range(len(buckets[i]) - 1, 0, -1):  # k 因为插入的是桶里面的  k个桶
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
            # 这个地方不就是是插入的时候直接排序了吗
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)  # buckets里面的元素是一个个列表 所以直接extend可以将这个列表加到sorted_li列表的后面
    return sorted_li


li2 = [random.randint(0, 10000) for _ in range(1000)]  # 生成一千个0-100的数
print(li2)
li3 = bucket_sort(li2)  # 会返回一个新的列表啊
print(li3)

"""
其他排序
    希尔排序
        是一种分组插入排序算法
        首先取一个整数d1=n/2，将元素分为d1个组 每组相邻两元素直接距离为d1，在各组内进行直接插入排序
        取第二个整数d2=d1/2，重复上述分组排序过程 知道di=1 即所有元素在同一组内进行直接插入排序
        希尔排序每趟并不使某些元素有序，而是使整体的数据越来越接近有序，最后一趟排序使得所有数据有序
        
        没有牛逼三人组快 但是比lowB三人组快
        希尔排序的时间复杂度讨论比较复杂 并且和选取gap序列有关
        最好的是 O(nlog2n)n乘以logn的平方
        
    计数排序
        O(n)
        假如列表中数的范围在0到100之间 设计时间复杂度为O(n)的算法 
        其实0-1000-10000是不是一样个道理啊
        
        限制
            就是要知道数的范围 到多少 创建一个这个数大小的列表
            消耗空间
            就比如 五个数 0和一亿那么开一亿的列表吗 
            不现实
    
    桶排序
        基于计数排序的
        首先将元素分在不同的桶中，在对每个桶中的元素排序
        这个数据大了确实也是慢 还不如用牛逼三人组
        平均时间复杂度是O(n+k)
        最坏情况时间复杂度O(n2k)
        空间复杂度O(nk)
        
    基数排序
        个位 十位 百位 依次来比 
        先按照个位数给他排序 小的在前面 再按照十位数来比小的在前面 再按照百位数 依次类推
        时间复杂度O(kn)
        空间复杂度O(k+n)
        这个和快排来说 当数量少的时候 基数排序快
        当k增加(这个是桶的或it的大小或者是值的大小)的多之后 快排还是快 n(代表问题的规模 就是多少个数) 
"""


#  基数排序
def radix_sort(li):
    max_num = max(li)  # 确定循环几次
    it = 0
    #  这个处理方法 牛逼把
    while 10 ** it <= max_num:  # k
        buckets = [[] for _ in range(10)]  # 这个地方分桶也是10个桶 因为0-9 放这个里面呗
        for var in li: # n
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)  # 这个地方是不是就是做了分桶啊
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新写回li
        it += 1
"""
    为什么没有排序就可以输出呢 因为先做个位数 然后按照桶比 
        是不是第一个桶里面是个位为0的 依次第二个桶里面是1 最后一个桶里面是9
        也就是说前面的桶比后面的桶的个位小  写回去之后是不是就是个位从小到大依次递增
    第二次走过来 
        比十位的 然后也是桶从0到9   
        输出你会发现 十位数从小到大递增 而且是不是刚刚说了个位数从小到大是依次递增的 
        这个地方你进去的话 是不是也是这样的 从小到大进去的吗 然后每个桶里面是不是就是个位从小到大的 然后十位都一样 十个桶里面十位从小到大
        然后写出来是不是就是十位依次递增了 但是每个对应的十位后面的个位数是不是都是依次递增的啊 
    最后一次
        是不是就是前面都是正常的了 
        把最高位的数拿过来比 从0输出(位数不够不就补0呗) 这样的话是不是可以依次增加了啊
        因为前面的数都搞好了呗
    这个过程多走几遍就知道了
"""

li4 = list(range(1000))
random.shuffle(li4)
print(li4)
radix_sort(li4)
print(li4)
