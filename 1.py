# for i in range (1,1000):
#    i % 3 = 0
#    i % 5 = 0

#    print (i)



'''def foo(a):
    if a == 4:
        print ("ba")
    else:
        print ("ya")



for i in range(10):
    print (i)
    foo(i)

'''


def foo(n):
    a = 0
    for x in range(1, n + 1):

        if x % 3 == 0:
            print(x, "Is divisible by 3")

            a = a + x

        elif x % 5 == 0:
            print(x, "Is divisible by 5")

            a = a + x

    print(a)


foo(1000)

