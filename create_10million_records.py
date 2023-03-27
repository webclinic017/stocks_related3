from datetime import datetime
startTime = datetime.now()
g='s'
mil=10
p=open('/home/az2/' + g + '.txt','w+')


k=0
for x in range(mil*1000000):
    k=k+1
##    print(x,"hhhhh",datetime.now()-startTime)
    p.write(str(x))
    p.write(' ;')
    p.write("hello elapsed time: ")
    p.write(' ;')
    p.write(str(datetime.now()-startTime))
    p.write('\n')
p.close()
print('no of lines written: ', k/1000000, ' million - Time elapsed',  str(datetime.now()-startTime))  
