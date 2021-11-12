def fibnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnaci(n - 1) + fibnaci(n - 2)


#     递归回头看 是不是不难

"""
    子问题的重复计算
"""


#  这个就是动态规划  递推式 重复子问题  这个里面的f已经存好了
def fib_no_re(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
    return f[n]


print(fib_no_re(5))

"""
    这个动态规划
        这个不是固定的算法 是一个算法思想
         这个就是动态规划  递推式(递归) 重复子问题(子问题存起来)
        就比如第二个斐波那契函数 那个子问题都存起来 都存到了列表f里面了啊
        当然了 你别认为这个函数执行完了之后这个列表还有值啊 是没有值的  
        意思是你500你是不是找前一个  那你前一个不还是找前一个 而for循环做的不就生成后一个 
        这个技巧是不是就是存起来值了啊  牛逼
"""
