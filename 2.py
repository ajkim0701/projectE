a = 1
b = 2
print (a)
print (b)
for x in range (8):



            c = a+b
            #print (c)
            a = b
            b = c

            if c % 2 == 0:
                print("even", c)

            else:
                print ("odd", c)


