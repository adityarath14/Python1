import re
var='g gd god good goood'
print(re.findall('gd',var))
print(re.findall('go*d',var))
print(re.findall('god*',var))
var='g go gdd godd goodd gooodd'
print(re.findall('gd*',var))