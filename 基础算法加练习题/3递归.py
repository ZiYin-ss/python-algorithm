# coding:utf-8
def hanoi(n, a, b, c):
    """
    :param n n个盘子:
    :param a:
    :param b:
    :param c  这三个是盘子的名称:
    :return:
    """
    # 这个地方要是会断点调试直接可以看清 但是我不会
    #  但是不影响你对这个地方的理解 就把递归还是个函数走进去看执行了什么 里面还有函数 走进去看执行了什么
    if n > 0:
        #  n-1个盘子 经过从a经过c移动到b
        hanoi(n - 1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n - 1, b, a, c)




hanoi(64, "A", "B", "C")

"""
    首先递归的特点 
        调用自身
        结束条件 
    汉诺塔移动次数的 递推式
        h(x)=2h(x-1)+1
        h(64) = xxx很多
"""
