


def is_prime (n):
    if n<=1:
        return False

    for x in range (2,n):
        y = n % x
        if y == 0:
            return False

    return True

c=0
n = 22
for i in range (2,int(n/2)+1):
    if i % 2 == 1 and is_prime (i):
        c=i
        print (c)
        
        







