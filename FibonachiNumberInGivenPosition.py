pos=5
f,s=0,1
if pos==1 or pos==2:
    print(pos-1)
else:
    for _ in range(pos-2):
        t=f+s
        f,s=s,t
    print(t)