d={}
try:
    d[['a',5,6]]=56
    print(d)
except Exception:
    print('Unhasable Type')