num=0
while num!=3:
    print(f'{num} is Outer Loop')
    number=7
    while number!=10:
        print(f'{number} is Ineer Loop')
        number+=1
    num+=1
    print('-'*20)