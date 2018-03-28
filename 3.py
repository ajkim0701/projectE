


def is_prime (n):
    if n<=1:
        return False

    for x in range (2,n):
        y = n % x
        if y == 0:
            return False

    return True


for i in range(0,20):
    a = is_prime(i)
    print (i, a)



