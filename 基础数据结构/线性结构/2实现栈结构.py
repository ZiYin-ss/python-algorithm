class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()  # 列表的pop方法就是弹出最后一个 返回回来

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]  # 这个地方是列表的-1 展示列表的最后一个元素 但不弹出
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)
print(stack.pop())
print(stack.stack)
print(stack.get_top())
print(stack.stack)


#  实现括号匹配问题
#  这个原理 你知道吗 就是说当进来左边的话 全部都可以进去 但是进来右边的话
#   都得看看栈顶和这个括号是否匹配 用字典做左右括号 右括号作为key 左括号是value
#  那么是不是右括号为key和你传进来得一样 取出值 要是一样得不就可以把栈最后一个弹出呗出来呗
#  要是不一样或者为空栈 还有值 不就是false
#  最后判断栈是空的话就是匹配完了呗  就true
def brance_match(s):
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
            else:  # stack.get_top() != match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brance_match('({})'))
