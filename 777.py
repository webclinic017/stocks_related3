f2=open('/home/az2/t5.txt','r+')
f3=open('/home/az2/t65.txt','w+')
i=0
for x in f2.readlines():
    i=i+1       
##    f3.write(x)
    f2.write(str(x).rstrip('\n')+str(' -').rstrip('\n'))
##    f3.write(str(i)+x+'kkkk')
##    f3.write(str(i)+x+'tttt')
    f3.write('\n\n')


f3.close()
f2.close()             


             
