def fun(lst,ave,Len):
    times = 0
    for i in range(Len-1):
        if lst[i] == ave:
            continue
        elif lst[i] <ave:
            num = min(lst[i+1],ave-lst[i])
            # 这个地方是这个意思 类似于借数  假如lst[i+1]小那么 lst[i] 最多不也只能借lst[i+1]的个数吗 对吧
            # 反之ave-lst[i] 小 那么不就可以借了吗  外面的while循环其实就是防止这种情况出现呢  确实是情况最小
            lst[i],lst[i+1]=lst[i]+num,lst[i+1]-num
            times+=1
        elif lst[i]>ave:
            lst[i+1] +=lst[i]-ave
            lst[i]=ave
            times+=1
    return lst,int(times)


lst=list(map(int,input().split(',')))
Len = len(lst)
ave = int(sum(lst)/Len)
lst1 = lst.copy()
time1 = 0
while lst1!=[ave]*Len:
    lst1,times = fun(lst1,ave,Len)
    time1+=times
    
lst2 = lst.copy()
lst2 = lst[::-1]  # 这个地方只是倒序一下 可能次数少一点
time2 = 0
while lst2!=[ave]*Len:
    lst2,times = fun(lst2,ave,Len)
    time2+=times
print(min(time1,time2))
