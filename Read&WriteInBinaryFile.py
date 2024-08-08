fobj=open('h2r.jpg','rb')
content=fobj.read()
gobj=open('dup.jpg','wb')
gobj.write(content)