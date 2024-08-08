def Sample(a):
    print(a)
    if a==5:
        return
    Sample(a+1)
a=1
Sample(a)