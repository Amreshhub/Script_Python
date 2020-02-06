import sys
print('File',sys.argv[0])
with open(sys.argv[0],'r') as f:
    for line in f:
        print(line,end ='')
        