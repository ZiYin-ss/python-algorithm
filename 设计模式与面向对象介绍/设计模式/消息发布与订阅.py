from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):  # 订阅者对象
    @abstractmethod
    def update(self, notice):
        pass


class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):  # 添加关注
        self.observers.append(obs)

    def detach(self, obs):  # 解除关注
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice):  # 发布者对象
    def __init__(self, company_info):
        super().__init__()
        self.company_info = company_info

    @property  # 负责读
    def company_info(self):
        return self.company_info

    @company_info.setter  # 负责写 就是写这个属性
    def company_info(self, info):
        self.company_info = info
        self.notify()  #推送


class Staff(Observer):  # 员工 具体的订阅者
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info
        # 这个地方的 等号左边的时自己的company_info
        # 等号右边的 是不是就是在notice类里面设置的方法notify for循环列表里面的每个Staff实例
        # 传进来的实例是不是就是StaffNotice的实例 它里面刚刚不是改了company_info
        #  是不是执行这个函数 更改我们自己的company_info 和StaffNotice中的company_info一样
        #  不难 很好理解 思想很好 可以借鉴

notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "今年业绩非常好给大家发奖金"
print(s1.company_info)

"""
    如果还理解不了 其实可以从上到下理解 
    发布者发布信息是company_info 然后更新属性(@company_info.setter) 
    更新的时候调用自身的提醒所有订阅者的功能(self.notify())  
    这个函数会遍历订阅者列表里面的一个个对象的更新方法(update)使得消息一致 
    传递的参数是不是就是自己实例本身(StaffNotice) 这个实例里面的消息和订阅者里面的一样
    所以说我们自己做的操作是不是就是说可以把这订阅者对象添加到订阅者列表里面(attach) 
"""