n1=int(input('Enter a Number:'))
n2=int(input('Enter another Number:'))
try:
    print(n1/n2)
except Exception:
    print("Can't Divide with zero")