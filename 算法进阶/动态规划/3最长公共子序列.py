def lcs_length(x,y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    print(x[0] == y[0])
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:  # 字符串位置从0开始的 ij位置字符匹配时候
                c[i][j] = c[i-1][j-1]+1
                # 是不是ij坐标的左上方啊 斜着的左上方 他的值加一啊
                # 假如第一次来的话 00位置是0 所以+1 11的位置上是1啊
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
            # 这个地方为什么这样写 因为你看图  就知道了 要确定前面有没有匹配到的 所以做标记


    return c[m][n]

print(lcs_length("ABCBDAB","BDCABA"))









"""
    一个有序的子序列是在该序列重删除若干元素后得到的序列 
    最长公共子序列 
        X = "ABBCBDE" Y="DBBCDB" LCS(X,Y) = "BBCD"
        暴力拆解 指数级别增长
    真不会
"""

"""
    其实框架是大的方面 其实算法更多的处理细节方面 细节做的速度快 那整个不就快了吗
"""



