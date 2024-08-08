import re
var='g go gdd godd goodd gooodd'
print(re.findall('go{4}d',var))
print(re.findall('go{2}d',var))
print(re.findall('go{2}d{3}',var))
print(re.findall('go{2,4}d',var))