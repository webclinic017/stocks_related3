
import numpy as np
from math import exp, log
from scipy.stats import norm
import matplotlib.pyplot as plt
import datetime as dt




b = dt.datetime(2021,7,15,23,59,59)
a = dt.datetime(2021,7,17,16,59,59)
f=((a-b).total_seconds()/(60*60*24)/365)*100

##print(f)

# Parameters
s = 3681.68 # current stock price
k = 3690 #strike price of the option in dollars
sigma = 0.2497 # constant volatility
r = 0.05 # constant interest rate
T = f # expiry date of contract, 2 years time

s=float(s)
k=float(k)

def V(s,T):
    return s * norm.cdf( (log(s / k) + (r + 0.5 * pow(sigma,2)) * T) / (sigma * np.sqrt(T)) ) 
    - k * exp(-r * T) * norm.cdf(  (log(s / k) + (r - 0.5 * pow(sigma,2.0)) * T) / (sigma * np.sqrt(T)) )

V_01 = V(s,T) # the value of our option at time t=0 is the same at expiry T

print (V_01)


# Parameters
s = 3681.68 # current stock price
k = 3700 #strike price of the option in dollars
sigma = 0.2497 # constant volatility
r = 0.05 # constant interest rate
T = f # expiry date of contract, 2 years time

s=float(s)
k=float(k)

def V(s,T):
    return s * norm.cdf( (log(s / k) + (r + 0.5 * pow(sigma,2)) * T) / (sigma * np.sqrt(T)) ) 
    - k * exp(-r * T) * norm.cdf(  (log(s / k) + (r - 0.5 * pow(sigma,2.0)) * T) / (sigma * np.sqrt(T)) )

V_02 = V(s,T) # the value of our option at time t=0 is the same at expiry T

print (V_02)

print(V_02-V_01)
##https://stackoverflow.com/questions/38361148/valueerror-math-domain-error-black-scholes-option-valuation
