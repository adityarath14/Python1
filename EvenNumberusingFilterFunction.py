def Even(ele):
    if ele%2==0:
        return True
print(list(filter(Even,range(10,21))))