#!/usr/bin/env python


def get_market_cap():
    import yfinance as yf
    import numpy as np
    from pandas_datareader import data
    import pandas as pd
    import pandas_datareader as web

    tickers=open('/home/az2/Downloads/tickers_33.txt','r')
    highcap=[]

    for x in tickers:
        print(x,yf.Ticker(x).info['marketCap'],yf.Ticker(x).info['sector'],yf.Ticker(x).info['currentPrice'])
##        market_cap_data = web.get_quote_yahoo(x)['marketCap']
##        print(market_cap_data)

def get_all_tickers():
    
    import ftplib
    import os
    import re
     
    # Connect to ftp.nasdaqtrader.com
    ftp = ftplib.FTP('ftp.nasdaqtrader.com', 'anonymous', 'anonymous@debian.org')
     
    # Download files nasdaqlisted.txt and otherlisted.txt from ftp.nasdaqtrader.com
    for ficheiro in ["nasdaqlisted.txt", "otherlisted.txt"]:
            ftp.cwd("/SymbolDirectory")
            localfile = open(ficheiro, 'wb')
            ftp.retrbinary('RETR ' + ficheiro, localfile.write)
            localfile.close()
    ftp.quit()
     
    # Grep for common stock in nasdaqlisted.txt and otherlisted.txt

    u=open('/home/az2/Downloads/tickers_33.txt','a+')
    for ficheiro in ["nasdaqlisted.txt", "otherlisted.txt"]:
            localfile = open(ficheiro, 'r')
            for line in localfile:
                    if re.search("Common Stock", line):
                            ticker = line.split("|")[0]
                            u.write(ticker)
                            u.write('\n')
                            print(ticker)
                            
                            # Append tickers to file tickers.txt
                            open("tickers.txt","a+").write(ticker + "\n")
    u.close()


def main():
    get_market_cap()


main()
    
