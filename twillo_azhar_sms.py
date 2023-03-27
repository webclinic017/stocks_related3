##from stocker import Stocker
##amazon = Stocker('AMZN')
##amazon.plot_stock()

##import datetime 
##from time import time, sleep
##i=1
##today = datetime.date.today()
##
##from datetime import datetime
##
##date_time = datetime.fromtimestamp(timestamp)
##d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
##while True:
##    sleep(5)
####    sleep(360 - time() % 60)
##    print(d,'   ',i)
##    i=i+1
##    if i >= 30:
##        break
# pip install twilio

# we import the Twilio client from the dependency we just installed
##from twilio.rest import Client
##
### the following line needs your Twilio Account SID and Auth Token
##client = Client("ACe9431de001f90edfba554532188cef6d", "4aad64be4c35d08341a198049da5f773")
##
### change the "from_" number to your Twilio number and the "to" number
### to the phone number you signed up for Twilio with, or upgrade your
### account to send SMS to any phone number
##client.messages.create(to="+16177120789", 
##                       from_="+12146955245", 
##                       body="Hello from Python!")
##
##


import os
from twilio.rest import Client
import time
import datetime 
from time import time




x = datetime.datetime.now()



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
##account_sid = os.environ['ACe9431de001f90edfba554532188cef6d']
##auth_token = os.environ['4aad64be4c35d08341a198049da5f773']
##client = Client(account_sid, auth_token)
client = Client("ACe9431de001f90edfba554532188cef6d", "4aad64be4c35d08341a198049da5f773")
message = client.messages \
                .create(
                     body="Join Earth "+str(x),
                     from_='+16177120789',
                     to='+12146955245'
                 )

print(message.sid)
