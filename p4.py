from subprocess import Popen, PIPE, STDOUT
import os

##cmd = 'cd /usr/lib/oracle/xe/app/oracle/product/10.2.0/server/bin && /etc/init.d/oracle-xe start && lsnrctl start'
##p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
##output = p.stdout.read()
##print ("", output,'\n')


cmd = 'cd /usr/lib/oracle/xe/app/oracle/product/10.2.0/server/bin'
p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
output = p.stdout.read()
print ('\n',"========================================",'\n', output,'\n')



cmd1 = '/etc/init.d/oracle-xe stop'
p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
output1 = p1.stdout.read()
print ('=========================================','\n')
print ("oracle starting",'\n')
print ("", output1,'\n')
print ('=========================================','\n')

cmd2 = 'lsnrctl stop'
p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
output2 = p2.stdout.read()
print ('=========================================','\n')
print (cmd2,'\n')       
print ("", output2,'\n')
print ('=========================================','\n')
