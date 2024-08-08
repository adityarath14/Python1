with open('f1.txt') as f2:
    print(f2.tell())
    print(f2.read(10))
    print(f2.tell())
    f2.seek(20)
    print(f2.tell())
    print(f2.read(10))