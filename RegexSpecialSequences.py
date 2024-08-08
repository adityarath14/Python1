import re
var='asty 34cv\nRT 27#\t$%892'
print(re.findall('\W',var))
var1='asty 34c_v\nRT 27#\t$%892'
print(re.findall('\w',var1))
print(re.findall('\S',var1))
print(re.findall('\s',var1))
print(re.findall('\D',var1))
print(re.findall('\d',var1))
s='aAbBcDdc'
print(re.findall('\Aa',s))
print(re.findall('a\A',s))
print(re.findall('c\Z',s))
print(re.findall('Dc\Z',s))
print(re.findall('Ddc\Z',s))
print(re.findall(r'\ba',s))
print(re.findall(r'a\b',s))
print(re.findall(r'dc\b',s))
print(re.findall(r'\Ba',s))
print(re.findall(r'a\B',s))
print(re.findall(r'dc\B',s))