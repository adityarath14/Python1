L=[10,20,60,19,23,18]
user=20
for ind in range(len(L)):
    if L[ind]==user:
        print(ind)
        break
else:
    print(-1)