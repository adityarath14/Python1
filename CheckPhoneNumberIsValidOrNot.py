import re
s='+91-8280952019'
if re.match('[+]91 [6789][0-9]{9}$|[+]91-[6789][0-9]{9}$',s):
    print('Valid')
else:
    print('Not Valid')