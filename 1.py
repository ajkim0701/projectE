'''Find the sum of all the multiples of 3 or 5 below 1000.
answer: 233168 '''
def foo(n):
    a = 0
    for x in range(1, n ):

        if x % 3 == 0:
            print(x, "Is divisible by 3")

            a = a + x

        elif x % 5 == 0:
            print(x, "Is divisible by 5")
    
            a = a + x

    print(a)


foo(1000)

