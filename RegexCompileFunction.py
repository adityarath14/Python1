import re
mp='Hello Hi Bye Good bye'
print(re.compile(mp))
a=re.compile('o')
print(re.findall(a,mp))
print(re.findall('o',mp))