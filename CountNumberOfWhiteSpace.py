with open('f1.txt') as file:
    count_ws=0
    for c in file.read():
        if c==' ':
            count_ws+=1
    print(f'Number of whiteSpace is:{count_ws}')