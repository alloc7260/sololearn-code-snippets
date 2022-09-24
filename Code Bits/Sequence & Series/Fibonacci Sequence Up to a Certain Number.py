num = int(input('Enter a positive number: '))
a1, a2, nextterm = 0, 1, 0
while nextterm <= num :
        print(nextterm)
        a1 = a2
        a2 = nextterm
        nextterm = a1 + a2