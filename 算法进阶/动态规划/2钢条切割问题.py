import time

"""这个叫自顶向下 递归都是这样的 自顶向下 n->n-1->n-2"""


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time:%s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


"""
    再说一遍装饰器的作用 
        cut_rod_recurision()
        执行这个函数的时候
            @的时候 实际上是执行了装饰器函数 把实际执行的这个函数作为参数  返回了wrapper(这一步其实比函数真正执行要快)
            其实 这个  cut_rod_recurision(xxx)  == wrapper(xxx)  这个xxx是不是到最后也是实际执行的这个函数的参数啊 
            只不过外面附加了点功能 
        
"""
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24,30]


def cut_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n - 1):
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n - i))
        #   传个2进去你就知道怎么走的了 就是p[2]=5 然后就是 max(5,1(本来是函数的但执行完之后其实就是返回1)+1)
        #     这样不就知道怎么走的吗  p[3] = 8  max(8,1+5(这个不就是传2进去了呗 ))
        #  这个递归其实还是有点难度的 想res返回的都是每个子问题的最优解 那组合是不是大问题的最优解
        #  想最底层会返回出什么东西  返回的是不是 p[1]的值 和p[2]的值的最大值 这样不就知道最大值是什么了吗
        return res


@cal_time
def c1(p, n):
    return cut_rod_recurision_1(p, n)


print(c1(p, 20))


def cut_rod_recurision_2(p, n):
    #  这个是只对右边剩下的一段继续切割 其实也一样
    #  因为左边切了一段不就是有固定的最大值 再找右边的呗
    #  而且每一次循环都会更新res res里面保存的一直都是最大值
    #  要是有合适的左边切的刚好就是符合最优解的时候左边的值 那么是不是就可以找到最优解的值 最大的会一直保存
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recurision_2(p, n - i))
        return res


@cal_time  # 装饰递归函数必须装饰器也是递归的  所以我们重写定义一个函数执行
def c2(p, n):
    return cut_rod_recurision_2(p, n)


print(c2(p, 20))

"""
    某公司出售钢条 出售价格与钢条长度之间关系 有个表
    现在有一段长度为n的钢条 和上面的价格表 求切割钢条方案 使得总收益最大
    
    最优子结构 
        可以将求解规模为n的原问题 划分为规模更小的子问题 完成一次切割后 可以将产生的两段钢条看成两个独立的钢条切割问题 
            以此类推
        组合两个子问题的最优解 并在所有可能的俩段切割方案重选取组合收益最大的 构成原问题的最优解
        钢条切割就满足最优子结构
            问题的最优解由相关子问题的最优解组合而成 这些子问题可以独立求解
        
        最优解总结就是说
            递推式 这个式子不好找
            
    cut_rod_recurision_1比cut_rod_recurision_2慢的多 O(2**n)
        可以想的到 就是cut_rod_recurision_2问题规模一下下去了好多
        但是说到底还是递归 效率极低 解决重复问题
"""

"""自底向上 n1->n2->n3"""


def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = p[i]
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
            # 这个有没有发现就是 p[i] 和p[j]+p[i-j]是这样的    好理解 不难 就是 第一个循环走完是p[1]的最优解
        #      第二个循环走完是p[2]的最优解  就这
        r.append(res)
    return r[n]   #O(n**2)
    #  n = 0 是0 n=1是
    # 这个不难 也好理解 就是说先把0这个段给他 再给1这个段最好的值给他
"""
    这个地方就是动态规划 就是说先算0在算1 再算2 等等
"""