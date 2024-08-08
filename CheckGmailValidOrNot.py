import re
s='rathaditya14@gmail.com'
if re.match('\w*[.]?\w*@gmail[.]com$',s):
    print('Valid')
else:
    print('Not Valid')