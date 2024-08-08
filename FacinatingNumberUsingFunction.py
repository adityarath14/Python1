def FN(num):
    check=str(num)+str(num*2)+str(num*3)
    for var in range(1,10):
        if str(var) not in check:
            return False
    return True
num=192
print('Facinating Number' if FN(num) else 'Not Facinating Number')