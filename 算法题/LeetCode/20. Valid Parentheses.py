# 有效的括号
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
"""
"""
    第一种使用栈
        左括号全部进去 右括号 字典判断栈第一个是不是 是的话就出来就是的了
        这样就可以保证要是右括号可以及时匹配到他需要的左括号
    第二种使用列表
        能不能想到匹配一个出去一个
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        match = {'}': '{', ']': '[', ')': '('}
        stack = Stack()
        for ch in s:
            if ch in {'(', '[', '{'}:
                stack.push(ch)
            else:
                if stack.is_empty():
                    return False
                elif stack.get_top() == match[ch]:
                    stack.pop()
                else:
                    return False
        if stack.is_empty():
            return True
        else:
            return False


class Solution1:
    def isValid(self, s: str) -> bool:
        match = {'}': '{', ']': '[', ')': '('}
        match_list = []
        for i in s:
            if i in {'(', '[', '{'}:
                match_list.append(i)
            else:
                if len(match_list) > 0 and match_list[-1] == match[i]:
                    # 这个地方必须要大于0 要不然 执行match_list[-1]其实会报错的
                    del match_list[-1]
                else:
                    return False
        if len(match_list) == 0:
            return True
        else:
            return False


"""
    这道题比较简单 就是注意 列表最后一个元素要和右括号匹配  就可以了 然后  匹配之后把列表最后一个删除 然后继续就可以
    注意索引出界 就是说 里面是0了 但是进来右括号之后 match_list[-1] 其实是 出界报错 注意      
"""

s = "()"
a = Solution1()
print(a.isValid(s))
