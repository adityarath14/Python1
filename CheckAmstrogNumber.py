var=153
copy=var
ans=0
c_digit=len(str(var))
while var!=0:
    ld=var%10
    ans=ans+ld**3
    var//10
if copy==ans:
    print('Amstrong Number')
else:
    print('NotAmstrong Number')