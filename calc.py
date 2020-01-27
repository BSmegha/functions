import calcmodule as c 
x=int(input("enter a number"))
y=int(input("enter a number"))
o=input("enter the operation")
if(o=='+'):
    print(c.add(x,y))
if(o=='-'):
    print(c.sub(x,y))
if(o=='*'):
    print(c.prod(x,y))
if(o=='/'):
    print(c.div(x,y))
