import sys
print('File',sys.argv[0])
with open('temp.txt','r') as f:
      s = f.readline()
      while s:
          print(repr(s))
          s = f.readline()
      