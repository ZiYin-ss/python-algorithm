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
