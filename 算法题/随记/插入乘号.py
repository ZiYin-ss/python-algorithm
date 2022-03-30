n = int(input())
num = input()
Len = len(num)
lst = []
for i in range(2**Len):
    if bin(i).count('1') == n and len(bin(i))-2<Len:
        sum1 = 1
        str_tmp = ''
        tempi = i
        for j in range(Len-1):
            str_tmp +=num[j]
            if tempi%2 ==1:
                sum1*=int(str_tmp)
                str_tmp = ''
            tempi=tempi>>1
        str_tmp += num[-1]
        sum1*=int(str_tmp)
        lst.append(sum1)

print(max(lst))