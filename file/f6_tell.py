import sys
print('File',sys.argv[0])
with open('temp.txt','r') as f:
      s = f.read(4)
      while s:
          print(repr(s))
          s = f.read(4)
          print("Pointer position:-", f.tell())
          print('Re read',f.read(4))
          
          f.seek(0)#Bring pointer to begging
          print('Re read 2',f.read(4))