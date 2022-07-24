n=5
k=0
for i in range(1,n+1):
 for j in range(1,2*n):
  if j in range(n-k,n+k+1) :
   print("*",end="")
  else :
   print(" ",end="")
 k+=1
 print()