def fibonachi(pos,f=0,s=1):
    if pos==1 or pos==2:
        return pos-1
    for _ in range(pos-1):
        t=f+s
        f,s=s,t
    return t
pos=5
print(fibonachi(pos))