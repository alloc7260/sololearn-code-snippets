n=5 #rows

for i in range(n):
 for j in range(i+1):
  print('*',end="")
 print()

print()

for i in range(n,0,-1):
 for j in range(i):
  print('*',end="")
 print()
 
print()

for i in range(n):
 for j in range(n-i-1):
  print(" ",end="")
 for k in range(i+1):
  print('*',end="")
 print()
 
print()

for i in range(n,0,-1):
 for j in range(n-i):
  print(" ",end="")
 for k in range(i):
  print('*',end="")
 print()
 
print()

for i in range(n):
 for j in range(n-i-1):
  print(" ",end="")
 for k in range(2*i+1):
  print('*',end="")
 print()

print()

for i in range(n,0,-1):
 for j in range(n-i):
  print(" ",end="")
 for k in range(2*i-1):
  print('*',end="")
 print()

print()

for i in range(n):
 for j in range(i+1):
  print('*',end="")
 print()
for i in range(n,0,-1):
 for j in range(i-1):
  print('*',end="")
 print()

print()

for i in range(n):
 for j in range(n-i-1):
  print(" ",end="")
 for k in range(i+1):
  print('*',end="")
 print()
for i in range(n-1,0,-1):
 for j in range(n-i):
  print(" ",end="")
 for k in range(i):
  print('*',end="")
 print()

print()

for i in range(n):
 for j in range(n-i-1):
  print(" ",end="")
 for k in range(2*i+1):
  print('*',end="")
 print()
for i in range(n,0,-1):
 for j in range(n-i+1):
  print(" ",end="")
 for k in range(2*i-3):
  print('*',end="")
 print()