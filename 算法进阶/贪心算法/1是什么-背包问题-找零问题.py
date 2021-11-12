#  找零问题
t = [100, 50, 20, 5, 1]  # 手上有什么面额的钱  别人给你钱 你打算怎么找


def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money  # 当前总额 除以钱的面额 向下取整是不是就是张数了啊
        n = n % money  # n%最大面额 的余数是不是可以继续找下一个面额来除啊
    #      假如要是小数 2.5之类的 是不是就是 循环之后 剩余五毛 n就是五毛啊
    #   11/5 为2张五块的 所以说整数是不是都可以处理啊 不难
    return m, n


print(change(t, 376))

"""
    贪心算法(贪婪算法)是指 在对问题求解时 总是做出在当前看来是最好的选择 
    也就是说 不从整体最优上加以考虑 他所做出的是在某种意义上的局部最优解
    贪心算法并不保证会得到最优解 但是在某些问题上 贪心算法的解就是最优解
    要会判断一个问题能否用贪心算法来计算

    贪心算法其实不难
        假如376 最多给你3个100的 当然也可以用6个五十的 但是最大最少 是不是可以用贪心 
        100的尽可能的处理 然后50的尽可能的处理 依次类推
"""

#  背包问题
"""
    一个小偷在某个商店发现有n个商品 第i个商品价值vi元 重wi千克 他希望拿走的价值尽量高 但他的背包最多只能容纳w千克的东西 
    他应该拿走哪些商品
    0-1背包(这个不用贪心算法 用不了)
        一个商品只能全部拿走 不能拿走一部分
    分数背包 
        对于一个商品 小偷可以拿走其中一部分 
"""

goods = [(60, 10), (100, 20), (120, 30)]  # 商品元组 前面是价格后面是重量
goods.sort(key=lambda x: x[0] / x[1], reverse=True)

#  这个是分数背包
def fraction_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += price
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * price
            w = 0
            break
    return m,total_v


print(fraction_backpack(goods, 50))

"""
    0-1背包还没有写
    会在动态规划那写
"""