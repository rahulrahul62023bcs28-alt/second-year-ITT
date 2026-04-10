a=input("enter the start datetime:")
b=input("enter the end datetime:")
c=int(a[11:13])
d=int(b[11:13])
e=d-c
if(e>5):
   e=e-1
   print(e)
else:
   print("invlaid")
