#  水壶问题
"""
有两个水壶，容量分别为jug1Capacity和 jug2Capacity 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到targetCapacity 升。
如果可以得到targetCapacity升水，最后请用以上水壶中的一或两个来盛放取得的targetCapacity升水。
你可以：
    装满任意一个水壶
    清空任意一个水壶
    从一个水壶向另外一个水壶倒水，直到装满或者倒空
"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        queue = [(0, 0)]
        seen = set((0, 0))

        while len(queue) > 0:
            a, b = queue.pop(0)
            if a == z or b == z or a + b == z:
                return True
            states = set()

            states.add((x, b))  # 3,0
            states.add((a, y))  # 0,5
            states.add((0, b))  # 0,0
            states.add((a, 0))  # 0,0
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a)))  # 0,0 看下面解析
            states.add((0 if a + b < y else a - (y - b), min(b + a, y)))  # 0,0
            for state in states:
                if state in seen:
                    continue
                queue.append(state)
                seen.add(state)
        return False


jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4

a = Solution()
print(a.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))
"""
y倒入x中(2 cases):  cur_x对应a cur_y对应b
    假设倒入水的容量为V：则y中剩余：cur_y-V；x中拥有：cur_x+V;
    若倒完之后y还有剩余，说明x已满：V=x-cur_x
    故在这种情况下：(x,cur_y+cur_x-x)
    若倒完之后y空了，说明：V=cur_y,
    故在这种情况下:(cur_x+cur_y,0)
x倒入y中(2 cases):
    与上面情况相似，得到：
    若倒完之后x还有剩余:(cur_x+cur_y-y,y)
    若倒完之后x空了:(0,cur_x+cur_y)
for (nbr_x,nbr_y) in [(cur_x,y),(cur_x,0),(x,cur_y),(0,cur_y),(x,cur_y+cur_x-x) if cur_x+cur_y>=x else (cur_x+cur_y,0),(cur_x+cur_y-y,y) if cur_x+cur_y>=y else (0,cur_x+cur_y)]:#y加满水/y排空水/x加满水/x排空水/y倒入x中(2 cases)/x倒入y中(2 cases)
"""