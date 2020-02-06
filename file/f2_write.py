with open('numbers.txt', 'w') as f:#CONTAXET MANAGER
    for i in range(10):
         f.write(str(i)+'\n')
    print(f.closed)
     
print(f.closed)