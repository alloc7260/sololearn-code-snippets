num = int(input('Enter the number of terms: '))
a1, a2, nextterm = 0, 1, 0
for i in range (num):
  print(nextterm)
  a1=a2
  a2=nextterm
  nextterm=a1+a2