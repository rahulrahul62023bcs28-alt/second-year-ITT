a=input("enter the email:")
b=len(a)
s=False
d=False
f=False
h=False
count1=0
count2=0
p=['!','#','$','%','^','&','*','(','/','-','+',')',',','?','}','{','>','<']
for i in range(b):
   if(a[i]=='@'):
      count1=count1+1
   if(a[i]=='.'):
      count2=count2+1
if count1==1:
   s=True

if count2>=1:
   d=True
if b!=0:
   f=True
if a not in p:
   h=True

g=s and d and f and h
if g==True:
   print("VALID")
else:
   print("INVALID")
