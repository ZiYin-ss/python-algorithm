def isa(li, i):
    if 2 not in li and 3 not in li and 5 not in li:
        return False
    for j in li:
        if j % 2 == 1 and j > 5 and j != i and j not in result:
            return False
    else:
        return True


result = []
for i in range(1, 101):
    if i == 1:
        result.append(i)
    else:
        a = []
        for j in range(1, i + 1):
            if i % j == 0:
                a.append(j)
        # print(a)
        if isa(a, i):
            result.append(i)

print(len(result))
