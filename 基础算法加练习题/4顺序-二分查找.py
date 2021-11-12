#  顺序查找
def linear_search(li,val):
    for index,value in enumerate(li):
        if val == value:
            return index
    else:
        return None

# 二分查找
def binary_search(li,val):
    left = 0
    right = len(li)-1
    while left <= right: #候选区有值
        mid = (left+right)//2   # 9//2=4  10//2=5 这个是下标
        print(mid)
        if li[mid] ==val:
            return mid
        elif li[mid]>val:   # 待查找的值在mid的左侧
            right = mid-1
        elif li[mid] <val:  # 待查找的值在mid的右侧
            left = mid +1
    else:
        return None

li = [1,2,3,4,5,6,7,8,9]
binary_search(li,3)  # 其实这个地方 看是很难看的 就是直接自己一步一步的走这个程序就可以了啊

print(li.index(2))

"""
    内置列表查找函数 index()
        这个是查找值在列表中的索引 
        li.index(2)  // 1 
        这个查找是线性查找 真的慢 
    顺序查找 (线性查找)
        从列表第一个元素开始 顺序进行搜索 直到找到元素或搜索到列表最后一个元素为止 
        O(n)
    二分查找 (折半查找)
        从有序列表的初始候选区li[0:n]开始，通过对待查找的值与候选区的中间值比较 可以使候选区减少一半
        二分查找的顺序要比线性查找的效率高 
        O(logn)
    假如要是2的32次方那么二分查找是不是每次都折半啊 就是除2呗 就是32次呗
    而顺序查找是不是就得2的32次方次
    
    总结
        有序列表查找用二分查找 效率不是一般的高 
        无序列表的查找 你得看你用的多不多 多的话 就排序 然后再二分查找
        少的话就算了 因为排序的时间复杂度和线性查找差不多
"""