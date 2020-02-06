import sys
print('File',sys.argv[0])
with open(sys.argv[0],'r') as f:
      s = f.read()
      print(repr(s))