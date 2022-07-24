n=5 #rows

q=0
for i in range(n,0,-1):
 p=1
 p+=q
 for j in range(i):
  print(p,end=" ")
  p+=1
 q+=1
 print()