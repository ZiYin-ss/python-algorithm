#  给两个字符串s和t 判断t是否为s的重新排列后组成的单词
def isAngram(s, t):
    dict1 = {}
    dict2 = {}
    for ch in s:
        #  这个取这个ch key的值 没有就设置默认值0 是不是就可以+1了啊
        #  我是真忘了这个方法
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1
    return dict1 == dict2
    # return sorted(list(s)) == sorted(list(t))


#  给定一个m*n的二维列表 查找一个数是否存在
#  每一行的列表从左到右已经排序好
#  每一行第一个数比上一行最后一个数大
#  就是有序的
def searchMatrix(matrix, target):
    h = len(matrix)
    if h == 0:
        return False
    w = len(matrix[0])
    if w == 0:
        return False
    left = 0
    right = w * h - 1
    while left <= right:
        mid = (left + right) // 2
        i = mid // w  # 在第几行
        j = mid % w  # 在第几列
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:  # 待查找的值在mid的左侧
            right = mid - 1
        else:  # 待查找的值在mid的右侧
            left = mid + 1
    else:
        return False


#  给定一个列表和一个整数 设计算法找到两个数的下标 使得两个数之和为给定的整数
#  保证肯定仅有一个结果
def binary_search(li, left, right, val):
    while left <= right:
        mid = (left + right) // 2
        if li[mid][0] == val:
            return mid
        elif li[mid][0] > val:
            right = mid - 1
        elif li[mid][0] < val:
            left = mid + 1
    else:
        return None


def twoSum(nums, target):
    new_nums = [[num, i] for i, num in enumerate(nums)]
    new_nums.sort(key=lambda x: x[0])  # 这个时间复杂度是nlogn
    for i in range(len(new_nums)):
        # for j in range(i+1,n): 方法一
        #   是不是查找 前面的已经和后面的都比过了 也不需要比了
        #   也不和自身比 那么是不是就可以说这个i和自己的下一个开始比啊 当然可以啊
        #     if nums[i]+nums[j] == target:
        #         return sorted([i,j])
        a = new_nums[i][0]
        b = target - a
        if b >= a:
            j = binary_search(new_nums, i + 1, len(new_nums) - 1, b)
        else:
            j = binary_search(new_nums, 0, i - 1, b)
        if j:
            return sorted([new_nums[i][1], new_nums[j][1]])
    #  nlogn
