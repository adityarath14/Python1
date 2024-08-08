import re
pp='ab*()cdK\nFR345^&*\t'
print(re.findall('^b',pp))
print(re.findall('^ab',pp))
print(re.findall('ab^',pp))