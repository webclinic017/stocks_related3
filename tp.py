from datetime import datetime
startTime = datetime.now()
g='p'
p=open('/home/az2/' + g + '.txt','w+')

for x in range(100000000):
##    print(x,"hhhhh",datetime.now()-startTime)
    p.write(str(x))
    p.write(' ;')
    p.write("hello elapsed time: ")
    p.write(' ;')
    p.write(str(datetime.now()-startTime))
    p.write('\n')
p.close()
print('Time elapsed',  str(datetime.now()-startTime))  
