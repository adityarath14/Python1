import re
s='H0ello 4every2one'
print(re.findall('e$',s))
print(re.findall('$e',s))
print(re.findall('one$',s))