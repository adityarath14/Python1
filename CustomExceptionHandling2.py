class AgeError(Exception):
    pass
age=int(input('What is your age:'))
name=input('what is your name')
try:
    if age>=18:
        print(f'{name} is eligible to vote')
    else:
        raise AgeError
except Exception:
    print(f'{name} not eligible to vote')