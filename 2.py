a = 1
b = 2
c=3
print (a)
print (b)
count= 2
#for x in range ():
while c < 4000000:


    c = a+b
    a = b
    b = c


    if c % 2 == 0:
        print("even", c)
        count=count+c
    else:
        print ("odd", c)


print (count)
