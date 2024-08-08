import re
mp='Hello Hi Bye Good bye'
print(re.finditer('o',mp))
print(list(re.finditer('o',mp)))
print(re.finditer('H',mp))
print(list(re.finditer('H',mp)))