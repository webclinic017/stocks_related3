##import sched
##import time,os
##
##scheduler = sched.scheduler(time.time, time.sleep)
##
##def print_event(name):
##    print ('EVENT:', time.time(), name)
##
##now = time.time()
##print ('STARTnn:', now)
##while True:    
##    scheduler.enterabs(now+2, 2, print_event, ('first',))
##    scheduler.enterabs(now+2, 1, print_event, ('second',))
##    time.sleep(5)
##scheduler.run()

import os
import time

import subprocess
i=0
while True:
    print(i,' start')
    subprocess.call('/home/az2/Downloads/binance/3/python-binance/ccxt_place_order2.py', shell=True)
    print(time,'    ',i)
    print(i,' complete')
    i=i+1
    time.sleep(62)

##i=0
##while True:
##    print(i,' Start running')
##    os.system('/home/az2/Downloads/binance/3/python-binance/ccxt_place_order2.py')
##    print(i, ' end')
##    i=i+1
##    time.sleep(62)
   
   
    


    
