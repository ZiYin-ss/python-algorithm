class File:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # 'dir' or 'file'
        self.children = []
        self.parent = None

    def __repr__(self):
        # 这个repr是重写显示的方法 同样这个也是个对象 也可以这样操作
        # for child in self.now.children:  # 显示不就是目录名
        #     if child.name == name:
        #         self.now = child  #可以now.里面的方法属性
        return self.name


n = File("hello")
n2 = File("hello1")
n.children.append(n2)
n2.parent = n


class FileTree:
    def __init__(self):
        self.root = File("/")
        self.now = self.root

    def mkdir(self, name):
        # name以文件结尾
        if name[-1] != "/":
            name += "/"
        node = File(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("找不到文件名")


tree = FileTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
print(tree.ls())
tree.cd("bin")
tree.mkdir("python")
print(tree.ls())

"""
    目录结构其实也是树结构 还有就是html里面的 html->body->div->xxx 这个不也是树结构吗
    二叉树的度 深度 子树 子节点 父节点就不说了
"""
