with open('file.csv','w')as Amresh:
        for i in range(10):
             print(i, i**2, i ** i, sep =',',file = Amresh)
             