
# Online Python - IDE, Editor, Compiler, Interpreter

import math
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))

delta=((b**2)-(4*a*c))
m=math.sqrt(delta)
x1=((-b)+m)/2*a
x2=((-b)-m)/2*a
if m>0:
 print(f"the value of x1 is :{x1}")
 print(f"the value of x2 is :{x2}") 
elif m==0:
 print(f"the value of x1 ix :{x1}") 
else:
 print("try again later")

