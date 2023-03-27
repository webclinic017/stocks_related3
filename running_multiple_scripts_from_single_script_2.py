from subprocess import run

import sys
import os

##os.system("grep -H -n 'plt.show()' /home/az2/*.py >> /home/az2/Downloads/b43b.txt")
##print(os.system("cat /home/az2/Downloads/b553.txt"))
##

##from subprocess import Popen, PIPE
##
##process = Popen(['swfdump', '/tmp/filename.swf', '-d'], stdout=PIPE, stderr=PIPE)
##stdout, stderr = process.communicate()

import subprocess as sp

# ok
pipe = sp.Popen('grep -H -n "pandas" /home/az2/Downloads/*.py', shell=True, stdout=sp.PIPE, stderr=sp.PIPE )
# res = tuple (stdout, stderr)
res = pipe.communicate()
print("retcode =", pipe.returncode)
print("res =", res)
print("stderr =", res[1])

sys.exit()

p=[]
for line in res[0].decode(encoding='utf-8').split('\n'):
##  print(line.split(':')[0])
  p.append(line.split(':')[0])

pp=[]
for x in p:
    if x not in pp:
      pp.append(x)

##print(pp)
p6a='/home/az2/Downloads/bbb42c.txt'      
p6=open(str(p6a),'w+')
for x in pp:
  p6.write(x)
  p6.write('\n')
  print(x)
p6.close()  







pg=[]
exclude_list=['/home/az2/798.py','/home/az2/799_b.py','/home/az2/799.py']
##f = open('/home/az2/Downloads/b43b.txt')
f=open(str(p6a),'r')
for x in f:
##    print(str(x).split(':')[0])
    if str(x).split(':')[0] in exclude_list:
        pass
    else:
##        pg.append(str(x).split(':')[0])
        pg.append(str(x))
    
pg2 = []
for i2 in pg:
    if i2 not in pg2:
        pg2.append(i2)
print(pg2,'   ',len(pg2))

##pg=['/home/az2/u7.py',
##    '/home/az2/jf17/uu9.py'
####    '/home/az2/trrrw.py'
##    ]

# which one_was working on: '/home/az2/jf17/uu9.py'
i=0
for x in pg2:
    print('Running ',x,'   ',i,'/',len(pg2))
##    subprocess.call(x, shell=True)
    run([sys.executable, str(x)])
    i=i+1

