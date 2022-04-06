# 简化路径
"""
给你一个字符串 path ，表示指向某一文件或目录的Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
请注意，返回的 规范路径 必须遵循下述格式：
始终以斜杠 '/' 开头。
两个目录名之间必须只有一个斜杠 '/' 。
最后一个目录名（如果存在）不能 以 '/' 结尾。
此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
返回简化后得到的 规范路径 。
"""


class Solution:  # 本来很简单 对吧 搞这些复杂的东西
    def simplifyPath(self, path: str) -> str:
        tmp = ''
        for i in range(len(path)):  # 处理多个/
            if i > 0 and path[i] == path[i - 1] == "/":
                continue
            tmp += path[i]
        tmp = tmp.rstrip('/')  # 去除最后一个字符串
        if tmp[0] != "/" or tmp[1] == tmp[2] == ".":  # 处理根目录指向问题
            return "/"
        print(tmp)
        ttmp = '/'
        lst = []
        for i in range(len(tmp)):  # "/home/foo"
            if tmp[i] != "/":
                ttmp += tmp[i]
            else:
                if len(lst) > 0 and ttmp == "/..":
                    lst.pop(-1)
                    ttmp = "/"
                    continue
                if len(lst) == 0 and ttmp == "/..":
                    ttmp = "/"
                    continue
                if ttmp == "/":
                    continue
                if ttmp == "/.":
                    ttmp = "/"
                    continue
                lst.append(ttmp)
                ttmp = "/"
        if len(lst) > 0 and ttmp == "/..":
            lst.pop(-1)
        if ttmp != '/.' or ttmp != '/..':
            lst.append(ttmp)
        print(lst)
        return ''.join(lst)


class Solution1:  # 本来很简单 对吧 搞这些复杂的东西
    def simplifyPath(self, path: str) -> str:
        ans = []
        for p in path.split("/"):
            if p == ".." and ans:
                ans.pop()
            elif p not in "..":
                ans.append(p)
        return "/" + "/".join(ans)


path = "/a/../../b/../c//.//"
a = Solution1()
print(a.simplifyPath(path))
