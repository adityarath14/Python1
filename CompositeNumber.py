num=int(input('Enter a number:'))
if num>1:
    fa_count=0
    for fa in range(1,num+1):
        if num%fa==0:
            fa_count+=1
    if fa_count!=2:
        print('Number is composite')
    else:
        print('Number is not composite')
else:
    print('Number is not composite')