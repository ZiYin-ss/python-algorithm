# z字型变换
"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z字形排列。
比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
PAHNAPLSIIGYIR
"""

"""
    这个解法的思想在于你能不能看出来 其实就是每一行的字符串拼接
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)
    """
        这个方法确实很牛逼 创建numRows个字符串呗放在列表里面 
        字符串开始循环 第一个放到数组第一个元素追加进去 一直循环到numRows个的时候 就把flag改为负的 放到前面的元素中去
        其实自己走一遍就知道了 原理就是走一个加一个 走到底就开始减一个
        延展一下可以就是蛇形填二维列表 判断flag决定添加的顺序    
    """

class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)