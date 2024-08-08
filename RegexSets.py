import re
var='g go gdd godd goodd gooodd'
print(re.findall('[g]',var))
print(re.findall('[go]',var))
print(re.findall('[go ]',var))
var1='as dfgSDF GER23 4$%^&not'
print(re.findall('[abc3]',var1))
print(re.findall('[a-z]',var1))
print(len(re.findall('[a-z]',var1)))
print(re.findall('[a-zA-z]',var1))
print(re.findall('[0-9]',var1))
print(re.findall('[a-zA-Z0-9]',var1))
print(re.findall('[^a-zA-Z0-9]',var1))
var2='44 99 5 34 87 1 0 22'
print(re.findall('[1-9][0-9]',var2))
print(re.findall('[1-9]',var2))
print(re.findall('[1-9][0-9][8]',var2))
var3='avcd*+Python'
print(re.findall('[+]',var3))
var4='^1234'
print(re.findall('\^',var4))