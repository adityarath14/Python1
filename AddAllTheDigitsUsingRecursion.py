def d_sum(num):
    if num==0:
        return 0
    return (num%10)+d_sum(num//10)
num=156
print(d_sum(num))