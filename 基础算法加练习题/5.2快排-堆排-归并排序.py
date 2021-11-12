import sys
import queue

sys.setrecursionlimit(100000)  # 设置递归最大深度


# 快速排序
# 快排的 partition函数
def partition(li, left, right):
    tmp = li[left]
    while left < right:  # O(n)
        #  下面必须要加上left<right 要不然就会冲突的
        #  如果不写的话 就是说right会为负值 有问题的
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边的空位上
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边的空位上面
    li[left] = tmp  # 这个地方 其实左右都一样的呢
    #  left和right值相等了 是不是就是第一个元素放到归位的元素上面了吧
    #  如此递归调用是不是就可以完成整个排序了啊
    #  因为一层一层的呗 先确定中间的 左边都小 右边都大 然后左边是一个新的继续这样
    #  偶数什么的没有关系 因为走法就不看偶数还是什么
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(li, 0, len(li) - 1)
print(li)


#  堆排序
#  堆排序调整函数  调整堆顶为最大的元素
def sift(li, low, high):
    """
    其实堆 说到底还是一个列表
    :param li:  列表
    :param low:  堆的根节点
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j是左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j位置有数就一直循环
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子比较大 指向右孩子
            j = j + 1  # 其实这个地方 还有就是为了比左右节点把谁放到父节点(领导节点上面啊)
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1  # 往下看一层  这样一直都能保证是不是最大的啊 主要是比较左右节点
        else:  # tmp更大 把tmp放到i的位置上面
            li[i] = tmp
            # 你看上面的 就是假如第一个就最大的话 是不是就是放回了原地啊
            # 要是在其他节点的时候 这个tmp就会放到空的 领导节点上啊
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上
    # 这个地方不要迷瞪啊 就是说这个地方每次的作用就是找出这个堆里面最大的那个元素
    # 然后给他存到其他地方去 然后把最后一个元素拿到放到堆顶 这个步骤不在这个函数里面体现的


def heap_sort(li):
    n = len(li)
    #  (n-2)//2这个是最后一个叶子节点的父节点下标
    for i in range((n - 2) // 2, -1, -1):
        # i是建堆的时候调整部分的根的下标
        sift(li, i, n - 1)
        # 建堆完成了
        # 其实这个建堆的过程就是说 先给了一个最小后面的叶子节点的父节点
        # 然后是不是有个根节点和子节点 然后就是比较和改位置啊 根节点和俩个子节点
        # i和j比较 然后换位置 然后最后没有了把小的那个放到空的i里面了啊  中间往下走了一级啊

        # 这个地方我一直再想假如要是根节点一直都不是最大的怎么办
        # 其实这种顾虑是多余的 建堆的时候 是不是领导节点都已经是最大的了
        # 你想啊 最大了之后 是不是放到堆顶的时候是不是就是左右两边最大的了 啊
        # 那为什么还有下面多余的几步呢 是不是为了比左右节点 确定把那个最大的放到领导节点啊
    for i in range(n - 1, -1, -1):
        # i是不是就是指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high  这个是不是就是说会把最大的元素放到0这个位置啊
    # 是不是这个for循环之后是不是就是说升序列表啊


li1 = [i for i in range(100)]
import random

random.shuffle(li1)
print(li1)
heap_sort(li1)
print(li1)

"""
排序NB三人组
    快速排序 quick_sort
        取一个元素P(一般是第一个) 使p元素归位
        列表被p分成两部分，左边都比p小 右边都比p大
        递归完成排序
            因为一层一层的呗 先确定中间的 左边都小 右边都大 然后左右边是一个新的继续这样
        O(nlogn)
        
        数越大比前面的三个lowB算法快得多
        
        快排的问题
            递归有最大深度的问题(999)
            最坏情况是O(n**2)
                比如[9,8,7,6,5,4,3,2,1]
                一次只会减少一个 怎么整 
                就是随便找个数跟第一个数交换行不行
            
            
    堆排序 heap_sort
        什么是堆
            大根堆
                父节点比子节点大
            小根堆
                子节点比父节点大
            堆的向下排序调整
                当根节点的左右子树都是堆时,可以通过一次向下的调整将其变换成一个堆
        堆排序
            建立堆，得到堆顶元素为最大元素
            去掉堆顶将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序，
            堆顶为第二大元素
            重复步骤3直到堆为空(就是第二句话)
        总结 
            这个地方确实不简单 是最难的 请注意 我上面的过程写的很详细了 大致已经分清了
            从heap_sort函数走 
            先建堆 主要是3个3个的走sift函数 这样是不是换位置和改
            这个地方先讲heap_sort函数比先讲sitf简单 
        O(nlogn)
        
        python内置模块是有堆排序的
            import heapq
            heapq.heapify(li) 建堆
            heapq.heappop(li) 往外弹出一个最小的元素 小根堆
            我们自己这个地方实现小根堆的话 是不是就是找3个节点里面最小的啊 
            先比较左右的值最小的和tmp比较最小的放到tmp那 while循环 就这了 
            
        topk问题
            现在有n个数 设计算法得到前k大的数
            排序后切片 O(nlogn)
            排序lowB三人组 O(kn)
            堆排序方法 O(nlogk)(m<n)
                取列表前k个元素建立一个小根堆 堆顶就是目前第k大的数
                依次向后遍历原列表 对于列表中的元素 如果小于堆顶则忽略该元素 
                如果大于堆顶 则将堆顶更换为该元素，并且对堆进行依次调整
                遍历列表所有元素后 倒序弹出堆顶
                for i in range(k,len(li)-1):
                    if li[i]>heap[0]
                        heap[0] = li[i]
                        sift(heap,0,k-1)
                大根堆很难实现的 但是直接遍历所有的 和这个一样 但是怎么比最小的呢 没法比
                
                
    归并排序
        分解 将列表越分越小 直至分成一个元素 
        终止条件 一个元素是有序的
        合并 将俩个有序列表归并 列表越来越大
        O(nlogn) 有n层就logn 每层就是一次while 所以是n 就是O(nlogn) 
        空间复杂度是O(n)
    
    python中的sort基于归并排序和插入排序的 
    
    总结
        快速排序最快
            但会有极端情况下效率最低
        堆排序最慢
            那为什么还用堆排序呢? 后面会说的
        归并排序会消耗额外的空间
        
        算法的稳定是指
            稳定的排序保证排完之后相对顺序是不变的 
            有顺序挨个换的都是稳定的 
            不挨个换的是不稳定的
"""


#  归并排序
def merge(li, low, high, mid):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    # while 执行完肯定有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high + 1] = ltmp  # 切片往回写


def merge_sort(li, low, high):
    if low < high:  # 至少有两个
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


li2 = [2, 4, 5, 7, 1, 3, 6, 8]
merge(li2, 0, 7, 3)
print(li2)
