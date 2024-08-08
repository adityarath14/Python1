def Happy(num):
    while num>9:
        d_sum=0
        while num!=0:
            rem=num%10
            d_sum+=rem**2
            num//=10
        num=d_sum
    return num==1 or num==7
print(list(filter(Happy,range(1,1001))))