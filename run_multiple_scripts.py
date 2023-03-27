#!/bin/bash
python3 /home/az2/stocks_Technicals56_with_signals22_v4.py ;
python3 volume_red_or_green_Hourly.py &

##import subprocess
##subprocess.call(['python3', '/home/az2/stocks_Technicals56_with_signals22_v4.py']) # Just run the program
##subprocess.check_output(['python3', '/home/az2/stocks_Technicals56_with_signals22_v4.py']) # Also gets you the stdout
##

##subprocess.call(['python3', '/home/az2/volume_red_or_green_Hourly.py']) # Just run the program
##subprocess.check_output(['python3', '/home/az2/volume_red_or_green_Hourly.py']) # Also gets you the stdout
##
##subprocess.call(['python3', '/home/az2/volume_red_or_green_Daily.py']) # Just run the program
##subprocess.check_output(['python3', '/home/az2/volume_red_or_green_Daily.py']) # Also gets you the stdout
