var=int(input('Enter a number:'))
rev=0
copy=var
while var!=0:
    rem=var%10
    rev=rev*10+rem
    var//=10
if copy==rev:
    print('Palaindrom')
else:
    print('Not Palindrom')