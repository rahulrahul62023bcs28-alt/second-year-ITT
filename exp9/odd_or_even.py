a=int(input("enter the number of eggs:"))
if a< 6:
   print("NO")
else:
   if a%2==0:
      c=a//6
      b=a%6
      d=b//2
      if d>=2:
         print("YES")
      else:
         print("NO")
   else:
      print("N is not even. this is not obeying the constraint")
