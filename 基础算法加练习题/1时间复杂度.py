print("hello world")

n = 10
for i in range(n):
    print("hello world")

for i in range(n):
    for j in range(n):
        print("hello world")

for i in range(n):
    for j in range(n):
        for m in range(n):
            print("hello world")

while n > 1:
    print(n)
    n = n // 2

"""
    2**6 = 64 log2**64 = 6
    64出结果6 只能用log啊 
    时间复杂度记为O(log2n)或O(logn)
    当算法出现循环折半的时候复杂度式子中会出现logn
    常见的时间复杂度
        O(1)<O(logn)<O(n)<O(nlogn)<O(n**2)<O(n**2logn)<O(n**3)
    复杂问题的时间复杂度
        O(n!) O(2**n) O(n**n)
    
    快速判断算法的复杂度
        确定问题规模n
        循环减半过程 ->logn
        K层关于n的循环 -> n**k
    复杂情况
        根据算法执行过程判断
    程序分为算法和数据结构 
    我们说程序的时间复杂度 其实有最好 最坏 一般  
    我们一般讨论一般和最坏
    
"""
"""
    顺序查找：从线性表的第一个元素开始查找，最好的情况是1，最坏的是n  平均n/2
    二分法查找：每次查找都减少一半的规模，只需要log(n,2)
    交换类排序：冒泡排序：俩俩相邻的数据元素之间的比较和交换，不断的消去逆序，知道所有数据元素有序为止最坏n(n-1)/2
    快速排序：在待排序的n个元素中取一个元素k 以元素k作为分割标准，把小于k的在前面，大于k的在后面。前后来个子表重复这样的过程。最坏n(n-1)/2
    简单插入类排序：开始时有序表只包含一个元素，无序表包含另外n-1个元素，每次取无序表中的第一个元素插入到有序表的正确位置。最坏n(n-1)/2
    希尔排序：最坏n**r
    简单选择排序：先从所有n个待排序的数据元素中选择最小的元素，将该元素与第一个元素交换，再从剩下的n-1个元素中找，依次类推。最坏n(n-1)/2
    堆排序：按顺序组成一个完全二叉树。最坏nlog（n，2）

"""