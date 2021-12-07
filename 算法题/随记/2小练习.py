#  斐波那契 其实这个地方可以用动态规划来写 就是加入到数组 第三个是第二个加第一个算出一个放到数组 依次类推
def fei(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fei(n - 1) + fei(n - 2)


def fei1(n):
    a = [0, 1]
    for i in range(2, n + 1):
        a.append(a[i - 1] + a[i - 2])

    return a[n]


print(fei(100))


#  阶乘
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
