import sys
import subprocess
import pandas as pd
import os

from subprocess import Popen, PIPE

ctrl_file="pink"
table_name="peter33c"
file_csv_data_name="emp35"
column_names="empno,name,pno"

##os.remove('/home/az2/Downloads/'+ctrl_file+'.ctl')
##cmd = ['touch', '/home/az2/Downloads/'+ctrl_file+'.ctl']
##a = subprocess.Popen(cmd, stdout=subprocess.PIPE)

cmd='ls'
##cmd = 'sqlldr userid=system/1 control=/home/az2/Downloads/pink.ctl' 
a = subprocess.Popen(cmd, stdin=subprocess.PIPE)
print(a)
