a=int(input("enter the number of marks to be stored:"))
print("enter the marks:")
b=[]
e={}

for i in range(a):
   c=int(input("enter the mark:"))
   b.append(c)
for j in range(len(b)):
   for k in range (len(b)):
      if b[j]==b[k]:
         count[j]=count[j]+1
   e[b[j]]=count[j]
print(e)
