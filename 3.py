def plusminus (a,b):
    x = a+b
    y = a-b
    return x, y

def is_prime (n):
    for x in range (2,n):
        y = n % x
        if y == 0:
            #print ("n, x, y", n, x, y)
            return False

    return True


for i in range(3, 15):
    a = is_prime(i)
    print (i, a)



