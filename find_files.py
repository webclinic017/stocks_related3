import glob
# All files ending with .txt
u="/home/az2/Downloads/*/*.py"
u2=glob.glob(u)


u3="/home/az2/*/*/*/*.py"
u4=glob.glob(u3)

i=0

p=open('/home/az2/Downloads/find_files.txt',mode='w+')
##for x in u2:
##    i=i+1
##    p.write(str(p))
##    print(i,' ',x)
##
##p.write('\n')
##p.write('\n')


for x in u4:
    i=i+1
    
    p.write(str(p))
    print(i,' ',x)    

p.close()
print('\n',i)
#ls -ld /home/az2/Downloads/*/*.py
