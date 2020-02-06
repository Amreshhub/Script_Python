import sys
print('File',sys.argv[0])
with open('temp.txt','r') as f:
      s = f.read(4)
      while s:
          print(repr(s))
          s = f.read(4)
      