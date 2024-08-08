s='RCB lost a Record'
print(s.count('o'))
print(s.count('cd'))
r='Yo Yo Honey Reddy'
print(r.index('o'))
print(r.index('o',2))
print(r.index('o',2,9))
g='abcabcdabca'
print(g.index('a',g.index('a')+1))
h='Jai Balayya'
print(h.find('l',4,7))
print(h.find('b',20,200))
print(h.find('i',2,5))
print(h.find('n'))
i='Aditya Rath'
print(sorted(i))
print(sorted(i,reverse=True))
print(sorted(i,reverse=False))
x='c'
print(x.isalpha())
y='8280952019'
print(y.isdigit())
z='143Aditya'
print(z.isalnum())
d='We are the future'
print(d.rindex('e'))
print(d.rindex('e',0,d.rindex('e')))
print(d.rfind('e'))
print(d.rfind('n'))
print(d.rindex('future'))
print(d.rindex('e',5,10))
k='i am the king'
print(k.startswith('i'))
print(k.startswith('i am ',0,3))
print(k.startswith('i am ',0,6))
print(k.startswith(' ',2,10))
print(k.endswith('king'))
print(k.endswith('h'))
print(k.endswith('king',0,13))
print(k.endswith('ing',10,12))
a=10
b=20
print(f'{a}+{b}={a+b}')
name='Adi'
age=23
salary=43000
print(f'{name} age is {age} and salary is {salary}')
name1='King'
salary1=100000
print('{} salary is {}'.format(name1,salary1))
print('{} salary is {}'.format(salary1,name1))
print('{1} is salary {0}'.format(name1,salary1))
print('{n} salary is {s}'.format(s=salary1,n=name1))
j=' abcd '
print(j.strip(' '))
print(j.rstrip(' '))
print(j.lstrip(' '))
o=' abcd ab '
print(o.strip(' '))