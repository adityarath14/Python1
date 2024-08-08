user_name=input('Enter the username')
password=input('Enter the password')
try:
    if password=='Aditya@8280':
        print('Login success')
    else:
        raise Exception
except Exception:
    print('Invalid Password')